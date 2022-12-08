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

datafile = "data/combine_contents.json"

with open(datafile , encoding='utf-8') as f:
	contents = json.load(f)

combine_contents = []

if __name__ == "__main__":

	googlemap_path = "https://www.google.co.kr/maps"

	for content in contents:

		restaurant_name = content['name']

		# search restaurant

		driver = webdriver.Edge(EdgeChromiumDriverManager().install())
		search_url = f'{googlemap_path}?q={restaurant_name}'
		driver.get(search_url)
		driver.implicitly_wait(time_to_wait=3)
		time.sleep(0.5)

		try:
			driver.find_element_by_xpath('//*[@aria-label="Reject all"]').click()
			driver.implicitly_wait(time_to_wait=10)
		except:
			print('no consent')
		finally:
			time.sleep(3)

		# address : Io6YTe fontBodyMedium
		address_list = driver.find_elements_by_xpath(".//div[@class='Io6YTe fontBodyMedium']")
		address = ''

		for item in address_list:

			if "강남" in item.text:
				address = item.text

		if address == '':
			print('no address found')
			continue

		print(restaurant_name)
		#print(address)

		current_url = driver.current_url
		start_index = current_url.index('@')
		tmp_coordinates = current_url[start_index+1:].split(',')
		latitude = tmp_coordinates[0]
		longitude = tmp_coordinates[1]

		# print(latitude)
		# print(longitude)


		# review 
		score = driver.find_elements_by_xpath(".//div[@class='fontDisplayLarge']")[0].text

		#print(score)

		# review link
		driver.find_elements_by_xpath(".//button[@class='HHrUdb fontTitleSmall rqjGif']")[0].click()
		time.sleep(2)
		review_link = driver.current_url

		#print(review_link)

		driver.close()

		content['score']['googlemap'] = score
		content['reviews']['googlemap'] = review_link
		content['coordinates'] = {"latitude" : latitude, "longitude" : longitude}

		combine_contents.append(content)

		print(content)


with open('data/new_combine_contents.json', 'w', encoding='utf-8') as json_file:
		json.dump(combine_contents, json_file , ensure_ascii=False)