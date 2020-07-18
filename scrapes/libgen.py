import requests 
from lxml import html
import random
from urllib.parse import quote
from bs4 import BeautifulSoup


def libgenscrape(topic):
    books_base = "/static/ico/book{}.jpg"
    books_urls = [books_base.format(k) for k in range(1,6)]
    random.shuffle(books_urls)
    libgen_home = "https://libgen.is"
    topic_name_parse = quote(topic)
    libgen_home_url = "https://libgen.is/search.php?req={topic}&open=0&res=25&view=simple&phrase=1&column=def"
    libgen_url = libgen_home_url.format(topic = topic_name_parse)
    print(libgen_url)
    pageContent=requests.get(libgen_url)
    # print(pageContent.text)
    soup = BeautifulSoup(pageContent.text, 'html.parser')
    print(soup)
    records = soup.findAll("tr", {"valign":"top"})
    # print(records)
    # reqd_path = '//li[@class="ais-InfiniteHits-item"]'
    # records = tree.xpath(reqd_path)
    print("Num of records on page:", len(records))
    top_5_records = records[1:6]
    return_list = []
    for i,record in enumerate(top_5_records):
        # print(str(record))
        # break
        data = {}
        record_soup = BeautifulSoup(str(record), 'html.parser')
        record_columns = record_soup.findAll("td")
        
        try:
            url_column = record_columns[2]
            url_column_soup = BeautifulSoup(str(url_column), 'html.parser')
            record_url = url_column_soup.findAll('a')[-1]
            record_link = libgen_home + "/" + record_url.get("href")
            print(record_link)
            data["link"] = record_link
        except:
            data["link"] = libgen_url

        try:
            author_column = record_columns[1]
            author_column_soup = BeautifulSoup(str(author_column), 'html.parser')
            author_name_url = author_column_soup.findAll('a')[0]
            author_name = author_name_url.contents[0]
            print(author_name) 
            data["partner"] = author_name
        except:
            data["partner"] = "Libgen"

        try:
            url_column = record_columns[2]
            url_column_soup = BeautifulSoup(str(url_column), 'html.parser')
            record_url = url_column_soup.findAll('a')[-1]
            record_title = record_url.contents[0]
            print(record_title)
            data["title"] = record_title
        except:
            data["title"] = topic
        
        try:
            # book_page = requests.get(data["link"])
            # image_soup = BeautifulSoup(book_page.text, 'html.parser')
            # image = image_soup.findAll('img')[0]
            # record_image_link = libgen_home + image.get('src')
            # print(record_image_link) 
            # data["image"] = record_image_link
            data["image"] = books_urls[i]
        except:
            data["image"] = ""
        
        data["color"]="lightblue"
        return_list.append(data)
        print("\n")

    return return_list

    

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = libgenscrape("data structures algorithms")

