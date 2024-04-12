import json
import requests


class IMDb:
    def __init__(self) -> None:
        config_address = "configs.json"
        f = open(config_address)
        self.configs = json.load(f)
        self.configs = self.configs["imdb_api"]

        self.find_url = self.configs["find_url"]
        self.detail_url = self.configs["detail_url"]

        self.headers = {
        	"X-RapidAPI-Key": self.configs["API-Key"],
        	"X-RapidAPI-Host": self.configs["API-Host"]
        }

    

    def find(self,query):
        querystring = {"query": query}
        response = requests.get(self.find_url, headers=self.headers, params=querystring)
        response = response.json()

        result = response["titleResults"]["results"]
        if (len(result)==0):
            return None
        
        result= result[0]
        id = result["id"]
        querystring = {"id": id}
        detail_resp = requests.get(self.detail_url, headers=self.headers, params=querystring)

        detail_resp = detail_resp.json()
        rate = detail_resp["ratingsSummary"]["aggregateRating"]
        genres = detail_resp["genres"]["genres"]
        genres = [g["text"] for g in genres]
        genres = ', '.join(genres)

        movie_detail = dict()
        
        movie_detail["title"] = result["titleNameText"]
        movie_detail["released_year"] = str(result["titleReleaseText"])
        movie_detail["genre"] = genres
        movie_detail["IMDB_rating"]= str(rate)
        movie_detail["overview"] = str()
        # print (genres)
        
        return movie_detail
        # print(response.json())