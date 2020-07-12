import requests 
from selenium import webdriver
from lxml import html
import time
from urllib.parse import quote
from bs4 import BeautifulSoup
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
import os
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager


GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

def youtubescrape(course_name):
    chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', 'chromedriver')
    edx_name_parse = quote(course_name)
    session = HTMLSession()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless") 
    chrome_options.binary_location = chrome_bin
    edx_home_url = "https://www.youtube.com"
    edx_url = "https://www.youtube.com/results?search_query=" + edx_name_parse

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
    driver.get(edx_url)
    records=[]
    while len(records)<5:
        htmlSource = driver.page_source
        soup = BeautifulSoup(htmlSource, 'html.parser')
        records = soup.findAll("ytd-video-renderer", {"class": "style-scope ytd-item-section-renderer"})
        print("Num of records on page:", len(records))
        top_5_records = records[:5]
        return_list = []
        for record in top_5_records:
            # print(str(record))
            # break
            data = {}
            record_soup = BeautifulSoup(str(record), 'html.parser')
            # print(record_soup)
            
            try:
                record_url = record_soup.findAll('a', {"class":"yt-simple-endpoint style-scope ytd-video-renderer"})
                record_link = edx_home_url + record_url[0].get("href")
                print(record_link)
                data["link"] = record_link
            except:
                data["link"] = edx_url

            try:
                record_name_span = record_soup.findAll("a", {"class":"yt-simple-endpoint style-scope yt-formatted-string"})
                record_partner_name = record_name_span[0].text
                print(record_partner_name) 
                data["partner"] = record_partner_name
            except:
                data["partner"] = "edx"

            try:
                record_course_title = record_soup.findAll("a", {"class":"yt-simple-endpoint style-scope ytd-video-renderer"})
                record_title = record_course_title[0].get("title")
                print(record_title) 
                data["title"] = record_title
            except:
                data["title"] = course_name
            
            try:
                record_image_div = record_soup.findAll("yt-img-shadow", {"class":"style-scope ytd-thumbnail no-transition"})
                image = BeautifulSoup(str(record_image_div[0]), 'html.parser').findAll('img')[0]
                record_image_link = image.get('src')
                print(record_image_link) 
                record_image_link= record_image_link.split("?")[0]
                
                data["image"] = record_image_link
            except:
                data["image"] = ""
            data["color"]="red"
            return_list.append(data)

            print("\n")

    
    # print(htmlSource)
    driver.close()

    # print(htmlSource.count("discovery-card Verified and Audit col col-xl-3 mb-4 scrollable-discovery-card-spacing"))

    
    # print(records)
    # reqd_path = '//li[@class="ais-InfiniteHits-item"]'
    # records = tree.xpath(reqd_path)
    

    return return_list

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = edxscrape("machine learning")