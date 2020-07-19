from apiclient.discovery import build 
import re
import os
   
# Arguments that need to passed to the build function 
DEVELOPER_KEY = os.environ.get('YOUTUBE_KEY')
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 
   
   
def youtube_search_keyword(query, max_results): 
       
    # calling the search.list method to 
    # retrieve youtube search results 
    
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
                                               maxResults = max_results).execute() 
       
    # extracting the results from search response 
    results = search_keyword.get("items", []) 
    youtube_url="www.youtube.com"
   
    # empty list to store video,  
    # channel, playlist metadata 
 
    return_list = []
    # extracting required info from each result object 
    for result in results: 
        # video result object 
        # print(result["kind"])
        # print(result)
        # print("\n")
        data = {}

        if result['id']['kind'] == "youtube#video" and query in result["snippet"]["title"]: 
            # print(result["snippet"]["title"])
            print(result["snippet"]["thumbnails"]["default"]["url"])
        
      
            # data["link"]="https://www.youtube.com/watch?v="+result["id"]["videoId"]
        
            try:
                data["link"] = "https://www.youtube.com/watch?v="+result["id"]["videoId"]
            except:
                data["link"] = youtube_url

            try:
                data["partner"] = result["snippet"]["channelTitle"]
            except:
                data["partner"] = "Youtube"

            try:
                # re.escape(result["snippet"]["title"])
                data["title"] = result["snippet"]["title"]
            except:
                data["title"] = query
            
            try:
                data["image"] = result["snippet"]["thumbnails"]["default"]["url"]
            except:
                data["image"] = ""
            data["color"]="red"
            return_list.append(data)
            print("\n")

    return return_list

            # videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
            #                 result["id"]["videoId"], result['snippet']['description'], 
            #                 result['snippet']['thumbnails']['default']['url'])) 
  
        # # playlist result object 
        # elif result['id']['kind'] == "youtube# playlist": 
        #     playlists.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
        #                          result["id"]["playlistId"], 
        #                          result['snippet']['description'], 
        #                          result['snippet']['thumbnails']['default']['url'])) 
  
        # # channel result object 
        # elif result['id']['kind'] == "youtube# channel": 
        #     channels.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
        #                            result["id"]["channelId"],  
        #                            result['snippet']['description'],  
        #                            result['snippet']['thumbnails']['default']['url'])) 

if __name__ == "__main__": 
    youtube_search_keyword('Geeksforgeeks', max_results = 10) 