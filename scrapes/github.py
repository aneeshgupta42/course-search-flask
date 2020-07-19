import requests



def scrapegithub(language):
    headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
    repos= requests.get("https://api.github.com/search/repositories?q="+language+"&sort=stars&order=desc", headers=headers)
    github_url="www.github.com"
    repos=repos.json()
    top_5_records = repos["items"][1:6]
    return_list = []
    for repo in top_5_records:
        print(repo)
        print("\n")
        # print(str(record))
        # break
        data = {}
        try:
            data["link"] = repo["html_url"]
        except:
            data["link"] = github_url

        try:
            data["partner"] = repo["owner"]["login"]
        except:
            data["partner"] = "GitHub"

        try:
            data["title"] = repo["name"]
        except:
            data["title"] = language
        
        try:
            data["image"] = repo["owner"]["avatar_url"]
        except:
            data["image"] = ""
        
        data["color"]="lightyellow"
        return_list.append(data)
        print("\n")

    return return_list

if __name__ == "__main__":
    # tree = scrape("computer vision")
    # tree = scrape("java")
    tree = github("data structures algorithms")