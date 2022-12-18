import random
import time
import pandas as pd
import requests
import os
import sys
import urllib.request
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
#from fake_useragent import UserAgent
import warnings
warnings.filterwarnings("ignore")

import json

#driver = webdriver.Edge(EdgeChromiumDriverManager().install())

region = "강남구"
encText = urllib.parse.quote(region + " 맛집")
display_num = 50
page_nums = 1

contents = []

# params = {'cookie' : 'NNB=LUURYNMJ4C6F6; nx_ssl=2; NRTK=ag#30s_gr#4_ma#2_si#2_en#2_sp#2; theme-promotion-november-notice-closed-count=1; page_uid=UJ0nKsp0YidssjcF2NRssssssf0-196483; BMR=s=1606280225697&r=https%3A%2F%2Fm.map.naver.com%2Fsearch2%2Fsearch.nhn%3Fquery%3D%25EC%2582%25AC%25EC%25A7%2581%25EB%258F%2599%2520%25EB%25A7%259B%25EC%25A7%2591%26sm%3Dhty%26style%3Dv5&r2=https%3A%2F%2Fm.map.naver.com%2Fsearch2%2Fsearch.nhn%3Fquery%3D%25EC%2582%25AC%25EC%25A7%2581%25EB%258F%2599%2520%25EB%25A7%259B%25EC%25A7%2591%26sm%3Dhty%26style%3Dv5; _naver_usersession_=SG1QrzcT5q6Ebt2OsL2srOJH; wcs_bt=sp_96fc91c9207ec0:1606394543|sp_9690f7f72d5c08:1606279853|80c9a70e2db3:1606225711',
# 	'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


for page_num in range(0, page_nums):

	url = f"https://map.naver.com/v5/api/search?caller=pcweb&query={encText}&type=all&searchCoord=126.93536503149417;37.576196000000024&page={str(page_num + 1)}&displayCount={display_num}&isPlaceRecommendationReplace=true&lang=ko"

	response = requests.get(url)
	datas = response.json()["result"]["place"]["list"]

	for data in datas:

		results = {}

		id = data['id']

		print('id : {}'.format(data['id']))

		naver_place_url = "https://m.place.naver.com/restaurant/{}/home".format(str(id))

		driver = webdriver.Edge(EdgeChromiumDriverManager().install())
		driver.get(naver_place_url)
		driver.implicitly_wait(time_to_wait=3)
		time.sleep(0.5)

		score = ""

		try:
			score = driver.find_elements_by_xpath(".//*[@class='PXMot LXIwF']/em")[0].text
		except:
			score = ""

		opening_hours = []

		try:

			hour_button = driver.find_elements(By.CLASS_NAME, "x8JmK")[1].click()
			time.sleep(0.1)
			elms = driver.find_elements(By.CLASS_NAME, "X007O")
		
			for i in range(1, len(elms)):
				opening_hours.append(elms[i].text)

			opening_hours[-1] = opening_hours[-1][:-3]

		except:
			opening_hours = []

		# remove 접기 word
		#print(opening_hours)

		try :
			driver.find_elements_by_xpath(".//*[@class='xHaT3']")[0].click()
			time.sleep(1)
			description = driver.find_elements_by_xpath(".//*[@class='zPfVt']")[0].text

		except:
			description = ''

		driver.close()

		results['name'] = data["name"]
		results['category'] = data["category"]
		results['address'] = data["address"]
		results['opening_hours'] = opening_hours
		results['score'] = score
		results['menu'] = data["menuInfo"]
		results['url'] = data["homePage"]
		results['reviews'] = "https://m.place.naver.com/restaurant/{}/review/visitor".format(str(id))
		results['thumbnails'] = data['thumUrls']
		results['description'] = description

		contents.append(results)
		print(results)

		time.sleep(1)

with open('data/naver_contents.json', 'w', encoding='utf-8') as json_file:
    json.dump(contents, json_file , ensure_ascii=False)