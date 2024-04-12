from redis_manager import Redis 
from elastic_manager import Elastic
from imdb_api_manager import IMDb
from flask import Flask, jsonify, request



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


app = Flask(__name__)   
movies = Movies()

@app.route('/query', methods=['GET'])
def handle_query():
    # Get the query parameter
    query = request.args.get('query', '')

    response = movies.find(query)
    # Create a JSON response

    return jsonify(response)


app.run(debug=True,host='0.0.0.0')