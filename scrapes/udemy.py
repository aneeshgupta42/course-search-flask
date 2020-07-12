import requests 
from lxml import html
from urllib.parse import quote
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
import time
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager




def udemyscrape(course_name):
    edx_name_parse = quote(course_name)
    session = HTMLSession()
    
    edx_home_url = "https://www.udemy.com"
    edx_url = "https://www.udemy.com/courses/search/?src=ukw&q="+ edx_name_parse
    # print(edx_url)
    # r = session.get(edx_url)
    pageContent=requests.get(edx_url)
    # r.html.render()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(edx_url)
    time.sleep(5)
    htmlSource = driver.page_source
    # print(htmlSource)
    soup = BeautifulSoup(htmlSource, 'html.parser')
    tree = html.fromstring(htmlSource)
    # print(tree)
    driver.close()
    # print(pageContent.text)
    soup = BeautifulSoup(htmlSource, 'html.parser')
    # print(soup)
    records = soup.findAll("div", {"class":"popover--popover--t3rNO popover--popover-hover--14ngr"})
    print(records)
    print("Num of records on page:", len(records))
    top_5_records = records[:5]
    return_list = []
    for record in top_5_records:
        # print(str(record))
        # break
        data = {}
        record_soup = BeautifulSoup(str(record), 'html.parser')
        
        try:
            record_url = record_soup.findAll('a', {"udlite-custom-focus-visible course-card--container--3w8Zm course-card--large--1BVxY"})
            record_link = edx_home_url+ record_url[0].get("href")
            print(record_link)
            data["link"] = record_link
        except:
            data["link"] = edx_url

        try:
            record_name_span = record_soup.findAll("div", {"class":"udlite-text-xs course-card--instructor-list--lIA4f"})
            record_partner_name = record_name_span[0].text  
            print(record_partner_name) 
            data["partner"] = record_partner_name
        except:
            data["partner"] = "Udemy"

        try:
            record_course_title = record_soup.findAll("div", {"class":"udlite-heading-sm udlite-focus-visible-target course-card--course-title--2f7tE"})
            record_title = record_course_title[0].text  
            print(record_title) 
            data["title"] = record_title
        except:
            data["title"] = course_name
        
        try:
            record_image_div = record_soup.findAll("div", {"class":"course-card--image-wrapper--Sxd90"})
            image = BeautifulSoup(str(record_image_div[0]), 'html.parser').findAll('img')[0]
            record_image_link = image.get('src')
            print(record_image_link) 
            data["image"] = record_image_link
        except:
            data["image"] = ""
        data["color"]="orangered"
        return_list.append(data)
    
        print("\n")

    return return_list

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = udemyscrape("data structures algorithms")
