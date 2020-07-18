import requests


def devscrape(name):
    return_list = []
   
    resp = requests.get('https://dev.to/api/articles/')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
     
    dev_url="https://dev.to"
    for article in resp.json():
        if name.lower() in article["tag_list"]:   
            data={}  
            try:
                data["link"] = article["url"]
            except:
                data["link"] = dev_urls

            try:
                data["partner"] = article["user"]["name"]
            except:
                data["partner"] = "Dev"

            try:
                data["title"] = article["title"]
            except:
                data["title"] = name
            
            try:
                if article["cover_image"] is None:
                    data["image"] = "https://i.ibb.co/GxtLLrM/g355ol6qsrg0j2mhngz9.png"
                else:
                    data["image"] = article["cover_image"]
            except:
                data["image"] = "https://i.ibb.co/GxtLLrM/g355ol6qsrg0j2mhngz9.png" 
            data["color"]="lightgrey"
            if data not in return_list:
                print(return_list)
                return_list.append(data)
                print("\n")

    return return_list


if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = devscrape('JavaScript')