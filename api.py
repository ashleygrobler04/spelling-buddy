from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
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
        return {
            "word": self.findWord()
        }


api.add_resource(helloWorld, "/")
if __name__ == "__main__":
    app.run(debug=True)
