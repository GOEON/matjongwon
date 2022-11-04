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
import json

warnings.simplefilter("ignore")


if __name__ == "__main__":
	num_mat_jib = 50

	# 서울 특별시 구 리스트
	# seoul_gu_list = [
	# 	"마포구",
	# 	"서대문구",
	# 	"은평구",
	# 	"종로구",
	# 	"중구",
	# 	"용산구",
	# 	"성동구",
	# 	"광진구",
	# 	"동대문구",
	# 	"성북구",
	# 	"강북구",
	# 	"도봉구",
	# 	"노원구",
	# 	"중랑구",
	# 	"강동구",
	# 	"송파구",
	# 	"강남구",
	# 	"서초구",
	# 	"관악구",
	# 	"동작구",
	# 	"영등포구",
	# 	"금천구",
	# 	"구로구",
	# 	"양천구",
	# 	"강서구",
	# ]

	seoul_gu_list = [
		"강남구"
	]
	kakaomap_path = "https://map.kakao.com/"
	result_cols = [
		"gu",
		"num_of_restaurants_in_gu",
		"name",
		"category",
		"score",
		"num_score",
		"review_link",
		"address",
		"operation_time",
		"menu_dict",
	]

	contents = []

	xpath_num_restaurant_gu = '//*[@id="info.search.place.cnt"]'
	xpath_place_list = '//*[@id="info.search.place.list"]'
	xpath_show_more = '//*[@id="info.search.place.more"]'
	xpath_next_page = '//*[@id="info.search.page.next"]'

	page_num = 1
	#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	driver = webdriver.Edge(EdgeChromiumDriverManager().install())
	for gu in tqdm(seoul_gu_list):
		# 카카오맵에서 검색어 입력한 페이지로 이동
		print(gu)
		search_url = f'{kakaomap_path}?q={gu + " 맛집"}'
		driver.get(search_url)
		driver.implicitly_wait(time_to_wait=3)
		time.sleep(0.5)

		# 해당 검색어의 장소 개수
		num_of_restaurants_gu = driver.find_element(
			by=By.XPATH, value=xpath_num_restaurant_gu
		).text

		clicked_show_more = False
		num_collected = 0
		while True:

			place_list = driver.find_element(by=By.ID, value="info.search.place.list")
			for place_elem in place_list.find_elements(By.TAG_NAME, value="li"):
				if place_elem.get_attribute("class") != "PlaceItem clickArea":
					continue

				name = place_elem.find_element(by=By.CLASS_NAME, value="link_name").text
				category = place_elem.find_element(
					by=By.CLASS_NAME, value="subcategory"
				).text
				score = place_elem.find_element(
					by=By.CLASS_NAME, value="rating"
				).text.split()[0]
				num_score = place_elem.find_element(
					by=By.CLASS_NAME, value="rating"
				).text.split()[1]
				review_link = place_elem.find_element(
					by=By.CLASS_NAME, value="numberofscore"
				).get_attribute("href")
				address = place_elem.find_element(
					by=By.CLASS_NAME, value="addr"
				).text.split("\n")[0]
				operation_time = place_elem.find_element(
					by=By.CLASS_NAME, value="openhour"
				).text.split("\n")[-1]

				place_elem.find_element(by=By.CLASS_NAME, value="moreview").send_keys(
					Keys.ENTER
				)
				driver.switch_to.window(driver.window_handles[-1])

				menu_dict = {}

				try:
					driver.find_element(by=By.CLASS_NAME, value="link_more").send_keys(
						Keys.ENTER
					)
				except:
					print(name, "  no more menu")

				try:
					menu_element = driver.find_element(
						by=By.CLASS_NAME, value="list_menu"
					)
					menu_name_list = menu_element.find_elements(
						by=By.CLASS_NAME, value="loss_word"
					)
					menu_price_list = menu_element.find_elements(
						by=By.CLASS_NAME, value="price_menu"
					)
					for menu_name, menu_price in zip(menu_name_list, menu_price_list):
						menu_dict[menu_name.text] = menu_price.text
				except:
					print("  menu exception")

				url = ""

				try:
					url = driver.find_elements_by_xpath(".//*[@class='link_homepage']")[0].get_attribute('href')

				except:
					print(" no url link")

				driver.close()
				driver.switch_to.window(driver.window_handles[0])

				result_dict = {}

				#result_dict["gu"].append(gu)
				#result_dict["num_of_restaurants_in_gu"].append(num_of_restaurants_gu)
				result_dict["name"] = name
				result_dict["category"] = category
				result_dict["address"] = address
				result_dict["opening_hours"] = operation_time
				result_dict["score"] = score
				#result_dict["num_score"].append(num_score)
				result_dict["menu"] = menu_dict
				result_dict["url"] = url
				result_dict["reviews"] = review_link
				print(num_collected + 1, name, category, score, num_score)
				num_collected += 1

				contents.append(result_dict)
				print(result_dict)

				if num_collected >= num_mat_jib:
					break

			if num_collected >= num_mat_jib:
				break

			if not clicked_show_more:
				driver.find_element(by=By.XPATH, value=xpath_show_more).send_keys(
					Keys.ENTER
				)
				clicked_show_more = True

			elif page_num % 5 == 0:
				driver.find_element(by=By.XPATH, value=xpath_next_page).send_keys(
					Keys.ENTER
				)

			else:
				xpath_page_num = f'//*[@id="info.search.page.no{page_num + 1}"]'
				driver.find_element(by=By.XPATH, value=xpath_next_page).send_keys(
					Keys.ENTER
				)

			page_num += 1
			time.sleep(1)

				

		print()

	#df = pd.DataFrame(result_dict, columns=result_cols)
	#df.to_csv("kakaomap_matjib_crawling.csv", index=False)

	driver.close()

	with open('kakaomap_contents.json', 'w', encoding='utf-8') as json_file:
		json.dump(contents, json_file , ensure_ascii=False)