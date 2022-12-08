# scraping TripAdvisor restaurants
# save reviews.csv in script directory 
# you can set number of restaurants to change num_restaurants value

'''
contents
name : String
category : string[] - 식당 유형
address : string
opening_hours : string
score : dictonary (str : str) {"kakao_map":"score", "tripadvisor": "score", "google_map" : "score"}  
menu : dictonary ( str : str) {"음식" : "가격"}
url : string - 식당 링크
reviews : string - 리뷰 링크


'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import os
import json

# open new windows by selenium
def OpenNewWindows(url):

	#driver = webdriver.Chrome(ChromeDriverManager().install())
	driver = webdriver.Edge(EdgeChromiumDriverManager().install())

	driver.get(url)
	driver.implicitly_wait(3)
	driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

	return driver

contents = []

# default tripadvisor website of restaurant
#url = "https://www.tripadvisor.com/Restaurants-g294197-Seoul.html"
#url = "https://www.tripadvisor.com/Restaurants-g294197-oa180-Seoul.html"#EATERY_LIST_CONTENTS
#url = "https://www.tripadvisor.com/Restaurants-g294197-zfn15565993-Seoul.html" #Gangnam-gu Restaurants
url = "https://www.tripadvisor.co.kr/Restaurants-g294197-zfn15565993-Seoul.html" # Korean gangnam-gu restaurants link

# default number of scraped restaurants
num_restaurants = 50
 
# number of restaurants in one page
num_restaurants_page = 30

split_word = ":"
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get(url)

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

# Need time to load the page.
time.sleep(0.5) 


for i in range(num_restaurants):

	restaurant_list = driver.find_elements_by_xpath(".//div[@data-test-target='restaurants-list']")

	list_name = '{}_list_item'.format(str(i+1))

	restaurant = restaurant_list[0].find_element_by_xpath(".//div[@data-test='{}']".format(list_name))
	link = restaurant.find_element_by_xpath(".//a[@class='Lwqic Cj b']").get_attribute('href')

	tmp_driver = OpenNewWindows(link)
	review_url = tmp_driver.current_url + "#REVIEWS"

	restaurant_name = ""
	score = ""
	categories = []
	website = ""
	opening_hours = ""
	address = ""

	try:
		for content in tmp_driver.find_elements_by_xpath(".//meta[@name='keywords']"):
			restaurant_name = content.get_attribute('content').split(',')[0]
	except:
		restaurant_name = ""

	try:
		for content in tmp_driver.find_elements_by_xpath(".//*[@class='UctUV d H0']"):
			review_rating = content.get_attribute('aria-label')
			score = review_rating.split(' ')[-1]
	except:
		score = ""

	try:
		for content in tmp_driver.find_elements_by_xpath(".//a[@class='dlMOJ']"):
			categories.append(content.text)
	except:
		categories = []

	try:
		for content in tmp_driver.find_elements_by_xpath(".//*[@class='YnKZo Ci Wc _S C AYHFM']"):
			website = content.get_attribute('href')
	except:
		website = ""

	try:
		for content in tmp_driver.find_elements_by_xpath(".//*[@class='yEWoV']"):
			address = content.text
			break
	except:
		address = ""

	# change live time the opening hours 
	# for content in tmp_driver.find_elements_by_xpath(".//span[@class='mMkhr']"):
	#     opening_hours = content.text

	#     start_index = opening_hours.find(split_word)
	#     opening_hours = opening_hours[start_index + 2:]

	#     break

	#titles = tmp_driver.find_elements_by_xpath(".//meta[@name='keywords']")[0].get_attribute('content').split(',')
	#review_rating = tmp_driver.find_elements_by_xpath(".//*[@class='UctUV d H0']")[0].get_attribute('aria-label')
	#categories = tmp_driver.find_elements_by_xpath(".//div[@class='SrqKb']")[0].text.split(',')
	#website = tmp_driver.find_elements_by_xpath(".//*[@class='YnKZo Ci Wc _S C AYHFM']")[0].get_attribute('href')
	#opening_hours = tmp_driver.find_elements_by_xpath(".//span[@class='mMkhr']")[0].text

	#address = tmp_driver.find_elements_by_xpath(".//a[@class='AYHFM']")[1].text
	#score = review_rating.split(' ')[-1]    

	#print('restaurant : {} '.format(restaurant_name))
	
	current_content = {}
	current_content["name"] = restaurant_name
	current_content["address"] = address
	current_content["score"] = score
	current_content["reviews"] = review_url
	current_content["category"] = categories[1:]
	current_content["url"] = website
	current_content["menu"] = ""
	current_content["opening_hours"] = opening_hours

	tmp_driver.close()

	# when scrap all restaurants in one page, need to go next page
	if (i + 1) % num_restaurants_page == 0:

		next_page_container = driver.find_element_by_xpath(".//div[@class='unified pagination js_pageLinks']")
		next_page_container.find_element_by_xpath(".//a[@class='nav next rndBtn ui_button primary taLnk']").click()

		time.sleep(1) 


	print(current_content)
	contents.append(current_content)


driver.close()

#print(contents)

with open('data/tripadvisor_contents.json', 'w', encoding='utf-8') as json_file:
    json.dump(contents, json_file , ensure_ascii=False)