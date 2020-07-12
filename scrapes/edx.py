import requests 
from selenium import webdriver
from lxml import html
import time
from urllib.parse import quote
from bs4 import BeautifulSoup
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager


def edxscrape(course_name):
    edx_name_parse = quote(course_name)
    edx_home_url = "https://www.edx.org"
    edx_url = "https://www.edx.org/search?tab=course&q=" + edx_name_parse
    print(edx_url)

    pageContent=requests.get(edx_url)
    htmlSource = pageContent.text

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(edx_url)
    time.sleep(7.5)
    htmlSource = driver.page_source
    # print(htmlSource)
    driver.close()

    print(htmlSource.count("discovery-card Verified and Audit col col-xl-3 mb-4 scrollable-discovery-card-spacing"))

    soup = BeautifulSoup(htmlSource, 'html.parser')
    records = soup.findAll("div", {"class": "discovery-card Verified and Audit col col-xl-3 mb-4 scrollable-discovery-card-spacing"})
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
        # print(record_soup)
        
        try:
            record_url = record_soup.findAll('a', {"class":"discovery-card-link"})
            record_link = edx_home_url + record_url[0].get("href")
            print(record_link)
            data["link"] = record_link
        except:
            data["link"] = edx_url

        try:
            record_name_span = record_soup.findAll("img", {"class":"partner-logo"})
            record_partner_name = record_name_span[0].get("alt") 
            print(record_partner_name) 
            data["partner"] = record_partner_name
        except:
            data["partner"] = "edx"

        try:
            record_course_title = record_soup.findAll("div", {"class":"discovery-card Verified and Audit col col-xl-3 mb-4 scrollable-discovery-card-spacing"})
            record_title = record_course_title[0].get("aria-label")  
            print(record_title) 
            data["title"] = record_title
        except:
            data["title"] = course_name
        
        try:
            record_image_div = record_soup.findAll("div", {"class":"d-card-hero"})
            image = BeautifulSoup(str(record_image_div[0]), 'html.parser').findAll('img')[0]
            record_image_link = image.get('src')
            print(record_image_link) 
            data["image"] = record_image_link
        except:
            data["image"] = ""
        data["color"]="grey"
        return_list.append(data)

        print("\n")

    return return_list

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = edxscrape("machine learning")

