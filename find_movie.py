from redis_manager import Redis 
from elastic_manager import Elastic
from imdb_api_manager import IMDb


class Movies:
    def __init__(self) -> None:
        self.redis = Redis()
        self.elastic = Elastic()
        self.imdb = IMDb()



    def find(self,query):
        result = self.redis.get_movie(query)
        if(result != None):
            print("redis has it!")
            return result
        result = self.elastic.search(query)
        if(result != None):
            print("elastic has it!")
            self.redis.add_movie(query,result)
            return result
        
        result = self.imdb.find(query)
        if(result != None):
            print("imdb has it!")
            self.redis.add_movie(query,result)
            return result
        print("ERROR: can't find it!")


if __name__ == '__main__':
    movies = Movies()
    rs = movies.find("friends")
    print(rs)