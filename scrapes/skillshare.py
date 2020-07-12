import requests 
from lxml import html
from urllib.parse import quote
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
import time
import chromedriver_binary
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
 
def skillsharescrape(course_name):
    chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', 'chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless") 
    chrome_options.binary_location = chrome_bin
    course_name_parse = quote(course_name)
    skillshare_home_url = "https://www.skillshare.com/"
    skillshare_url = "https://www.skillshare.com/search?query=" + course_name_parse

    pageContent=requests.get(skillshare_url)
    htmlSource = pageContent.text

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
    driver.get(skillshare_url)
    records=[]
    while len(records)<5:
        htmlSource = driver.page_source
        soup = BeautifulSoup(htmlSource, 'html.parser')
        records = soup.findAll("div", {"class":"ss-card ss-class"})
        if len(records)==0:
            return []
    #time.sleep()
    htmlSource = driver.page_source
    driver.close()
    # print(pageContent.text)
    #print(records)
    # print(records)
    # reqd_path = '//li[@class="ais-InfiniteHits-item"]'
    # records = tree.xpath(reqd_path)
    print("Num of records on page:", len(records))
    top_5_records = records[:5]
    return_list = []
    for record in top_5_records:
        # print(str(record))
        # break
        data = {}
        record_soup = BeautifulSoup(str(record), 'html.parser')
        
        # Page link
        try:
            record_url = record_soup.findAll('a', {"class": "ss-card__thumbnail js-class-preview"})
            #print(record_url)
            record_link = record_url[0].get("href")
            #print(record_link)
            data["link"] = record_link
        except:
            data["link"] = skillshare_url

        #Name of institution offering
        try:
            record_name_span = record_soup.findAll("a", {"class":"link-main no-bold title-link initialized"})
            record_partner_name = record_name_span[0].text  
            print(record_partner_name) 
            data["partner"] = record_partner_name
        except:
            data["partner"] = "skillshare"

        #Course Title
        try:
            record_course_title = record_soup.findAll("p", {"class":"ss-card__title"})
            record_title = record_course_title[0].text.strip()  
            print(record_title) 
            data["title"] = record_title
        except:
            data["title"] = course_name
        
        #Image link
        try:
            record_image_div = record_soup.findAll("div", {"class":"ss-card__thumbnail-img-holder"})
            image = BeautifulSoup(str(record_image_div[0]), 'html.parser').findAll('img')[0]
            record_image_link = image.get('src')
            print(record_image_link) 
            data["image"] = record_image_link
        except:
            data["image"] = ""
        data["color"]="yellow"
        return_list.append(data)
        print("\n")

    return return_list

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = skillsharescrape("python")
    print(tree)

