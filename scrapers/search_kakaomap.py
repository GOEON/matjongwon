import json
import time
import warnings
from collections import defaultdict

import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

warnings.simplefilter("ignore")

datafile = "data/naver_contents.json"

with open(datafile , encoding='utf-8') as f:
	naver_contents = json.load(f)

#print(d)

combine_contents = []

kakaomap_path = "https://map.kakao.com/"

for content in naver_contents:

	restaurant_name = content['name']

	driver = webdriver.Edge(EdgeChromiumDriverManager().install())
	search_url = f'{kakaomap_path}?q={restaurant_name}'
	driver.get(search_url)
	driver.implicitly_wait(time_to_wait=3)
	time.sleep(0.5)

	try :
		place_list = driver.find_element(by=By.ID, value="info.search.place.list")
		place_elem = place_list.find_elements(By.TAG_NAME, value="li")[0]
	except:
		print('{} is not avaliable in kakaomap'.format(restaurant_name))
		time.sleep(1)
		driver.close()
		continue

	for place_elem in place_list.find_elements(By.TAG_NAME, value="li"):

		try :
			address = place_elem.find_element(
				by=By.CLASS_NAME, value="addr"
			).text.split("\n")[0]
		except:
			print('invalid address')
			continue

		if '강남' not in address:
			continue

		score = place_elem.find_element(
			by=By.CLASS_NAME, value="rating"
		).text.split()[0]
		review_link = place_elem.find_element(
			by=By.CLASS_NAME, value="numberofscore"
		).get_attribute("href")


		naver_score = content['score']

		#del content['score']
		content['score'] = {}
		content['score']['navermap'] = naver_score
		content['score']['kakaomap'] = score

		naver_review_link = content['reviews']

		#del content['reviews']
		content['reviews'] = {}
		content['reviews']['navermap'] = naver_review_link
		content['reviews']['kakaomap'] = review_link

		combine_contents.append(content)

		time.sleep(1)

		driver.close()

		print(content)

		break


with open('data/combine_contents.json', 'w', encoding='utf-8') as json_file:
		json.dump(combine_contents, json_file , ensure_ascii=False)