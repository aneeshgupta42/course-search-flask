import requests 
from lxml import html
from urllib.parse import quote
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
import time




def edxscrape(course_name):
    edx_name_parse = quote(course_name)
    session = HTMLSession()
    
    edx_home_url = "https://www.udemy.com"
    edx_url = "https://www.udemy.com/courses/search/?src=ukw&q="+ edx_name_parse
    print(edx_url)
    # r = session.get(edx_url)
    pageContent=requests.get(edx_url)
    # r.html.render()
    driver = webdriver.Firefox()
    driver.get(edx_url)
    time.sleep(5)
    htmlSource = driver.page_source
    print(htmlSource)
    driver.close()
    # print(pageContent.text)
    soup = BeautifulSoup(pageContent.text, 'html.parser')
    records = soup.findAll("div", {"class":"discovery-card professional-certificate col col-xl-3 mb-4 scrollable-discovery-card-spacing"})
    print(records)

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = scrape("data structures algorithms")