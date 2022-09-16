# scraping TripAdvisor restaurants
# scraping contents : 이름, 위치, 평가, 사진
# save reviews.csv in script directory 
# you can set number of restaurants to change num_restaurants value

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import csv
import os

# open new windows by selenium
def OpenNewWindows(url):

    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(url)
    driver.implicitly_wait(8)
    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    return driver

# default path to file to store data
path_to_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "reviews.csv")

# Open the file to save the review
csv_file = open(path_to_file, 'w', encoding="utf-8")
csv_writer = csv.writer(csv_file)

header = ['name', 'address', 'raiting', 'photo1', 'photo2']
csv_writer.writerow(header) 

# default tripadvisor website of restaurant
url = "https://www.tripadvisor.com/Restaurants-g294197-Seoul.html"

# default number of scraped restaurants
num_restaurants = 60
 
# number of restaurants in one page
num_restaurants_page = 30

word = "rated"
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get(url)

driver.implicitly_wait(8)
driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

# Need time to load the page.
time.sleep(2) 

for i in range(num_restaurants):

    restaurant_list = driver.find_elements_by_xpath(".//div[@data-test-target='restaurants-list']")

    list_name = '{}_list_item'.format(str(i+1))

    restaurant = restaurant_list[0].find_element_by_xpath(".//div[@data-test='{}']".format(list_name))
    link = restaurant.find_element_by_xpath(".//a[@class='Lwqic Cj b']").get_attribute('href')

    tmp_driver = OpenNewWindows(link)

    titles = tmp_driver.find_elements_by_xpath(".//meta[@name='keywords']")[0].get_attribute('content').split(',')
    description = tmp_driver.find_elements_by_xpath(".//meta[@name='description']")[0].get_attribute('content')
    address = tmp_driver.find_elements_by_xpath(".//a[@class='AYHFM']")[1].text

    photo_container = tmp_driver.find_elements_by_xpath(".//div[@class='large_photo_wrapper   ']")

    photo_links = []

    for photo in photo_container:

        photo_link = photo.find_element_by_xpath(".//img[@class='basicImg']").get_attribute('src')

        photo_links.append(photo_link)

    title = titles[0]
    
    start_index = description.find(word)
    end_index = start_index + len(word)
    rating = description[end_index + 1:].split(' ')[0]

    print('restaurant : {} '.format(title))
    
    if len(photo_links) >= 2:
        csv_writer.writerow([title, address, rating, photo_links[0], photo_links[1]]) 
    elif len(photo_links) == 1:
        csv_writer.writerow([title, address, rating, photo_links[0], ""]) 
    else:
        csv_writer.writerow([title, address, rating, "", ""]) 

    tmp_driver.close()

    # when scrap all restaurants in one page, need to go next page
    if (i + 1) % num_restaurants_page == 0:

        next_page_container = driver.find_element_by_xpath(".//div[@class='unified pagination js_pageLinks']")
        next_page_container.find_element_by_xpath(".//a[@class='nav next rndBtn ui_button primary taLnk']").click()

        time.sleep(5) 



driver.close()
csv_file.close()