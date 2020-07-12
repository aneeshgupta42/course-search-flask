import requests 
from lxml import html
from urllib.parse import quote
from bs4 import BeautifulSoup


def courserascrape(course_name):
    course_name_parse = quote(course_name)
    coursera_home_url = "https://www.coursera.org"
    coursera_url = "https://www.coursera.org/search?query=" + course_name_parse
    print(coursera_url)
    pageContent=requests.get(coursera_url)
    # print(pageContent.text)
    soup = BeautifulSoup(pageContent.text, 'html.parser')
    records = soup.findAll("li", {"class":"ais-InfiniteHits-item"})
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
        
        try:
            record_url = record_soup.findAll('a', {"data-click-key":"search.search.click.search_card"})
            record_link = coursera_home_url + record_url[0].get("href")
            print(record_link)
            data["link"] = record_link
        except:
            data["link"] = coursera_url

        try:
            record_name_span = record_soup.findAll("span", {"class":"partner-name"})
            record_partner_name = record_name_span[0].text  
            print(record_partner_name) 
            data["partner"] = record_partner_name
        except:
            data["partner"] = "Coursera"

        try:
            record_course_title = record_soup.findAll("h2", {"class":"color-primary-text card-title headline-1-text"})
            record_title = record_course_title[0].text  
            print(record_title) 
            data["title"] = record_title
        except:
            data["title"] = course_name
        
        try:
            record_image_div = record_soup.findAll("div", {"class":"image-wrapper"})
            image = BeautifulSoup(str(record_image_div[0]), 'html.parser').findAll('img')[0]
            record_image_link = image.get('src')
            print(record_image_link) 
            data["image"] = record_image_link
        except:
            data["image"] = ""
        data["color"]="lightblue"
        return_list.append(data)
        print("\n")

    return return_list

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = courserascrape("data structures algorithms")

