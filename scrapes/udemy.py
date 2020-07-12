from requests_html import HTMLSession
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import chromedriver_binary
from urllib.parse import quote
from webdriver_manager.chrome import ChromeDriverManager

def udemyscrape(course_name):
    edx_name_parse = quote(course_name)
    session = HTMLSession()
    
    edx_home_url = "https://www.udemy.com"
    edx_url = "https://www.udemy.com/courses/search/?src=ukw&q="+ edx_name_parse
    print(edx_url)
    # r = session.get(edx_url)
    pageContent=requests.get(edx_url)
    # r.html.render()
    driver = webdriver.Chrome(ChromeDriverManager().install())
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
    tree = udemyscrape("data structures algorithms")
