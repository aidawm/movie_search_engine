from redis_manager import Redis 
from elastic_manager import Elastic


class Movies:
    def __init__(self) -> None:
        self.redis = Redis()
        self.elastic = Elastic()



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



if __name__ == '__main__':
    movies = Movies()
    rs = movies.find("Lifeboat")
    print(rs)