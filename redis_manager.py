import redis
import json

class Redis:
    def __init__(self) -> None:
        config_address = "configs.json"
        f = open(config_address)
        self.configs = json.load(f)
        self.configs = self.configs["redis"]

        self.rd = redis.Redis(host=self.configs["host"], port=self.configs["port"], decode_responses=True)
    
    def add_movie(self,query,movie_dict):
        self.rd.hset(query, mapping=movie_dict)

    def get_movie(self,movie_name):
        res= self.rd.hgetall(movie_name)
        if (len(res)== 0):
            return None

        else:
            return res
        