from elasticsearch import Elasticsearch
import json


class Elastic:
    def __init__(self) -> None:
        config_address = "configs.json"
        f = open(config_address)
        self.configs = json.load(f)
        self.configs = self.configs["elasticsearch"]

        self.es = Elasticsearch(self.configs["address"],    basic_auth=(self.configs["username"], self.configs["password"]) ,verify_certs=False)

    def search(self,query):

        resp = self.es.search(index=self.configs["index"], body={
                    "query": {
                        "match": {
                            "Series_Title": query
                        }
                    }
                })
        
        result = resp["hits"]["hits"]
        if (len(result) == 0):
            return None

        result= result[0]['_source'] 
    
        movie_detail = dict()
        
        movie_detail["title"] = result["Series_Title"]
        movie_detail["released_year"] = str(result["Released_Year"])
        movie_detail["genre"] = result["Genre"]
        movie_detail["IMDB_rating"]= str(result["IMDB_Rating"])
        movie_detail["overview"] = result["Overview"]

        return movie_detail
