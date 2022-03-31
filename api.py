from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import random

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


class helloWorld(Resource):
    def __init__(self):
        self.wordList = []
        with open("words.txt", "r") as f:
            words = f.read()
            self.wordList = words.split('\n')

    def findWord(self):
        self.choice = random.randint(0, len(self.wordList)-1)
        currentWord = self.wordList[self.choice]
        return currentWord

    def get(self):
        response = jsonify({'word': self.findWord()})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response


api.add_resource(helloWorld, "/")
if __name__ == "__main__":
    app.run(debug=True)
