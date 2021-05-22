# READING FROM INTERNET
from urllib import request  # OR import urllib

# OPEN URL
r = request.urlopen("http://www.google.com")
# STATUS CODE
print(r.getcode())
# READ WHOLE DATA
print(r.read())

# FETCHING JSON FORMAT FROM INTERNET
import json

url = "http://official-joke-api.appspot.com/random_ten"
req = request.urlopen(url)
print(req.getcode())
data = req.read()
# LOADING JSON
jsonData = json.loads(data)
print(jsonData)


# LOOPING THROUGH WHOLE JSON TO EXTRACT CERTAIN KEYS AND PUT IN A CLASS
class Joke:

    def __init__(self, setup, punchLine):
        self.setup = setup
        self.punchLine = punchLine

    def __str__(self):
        return f"Setup = {self.setup}, PunchLine ={self.punchLine}"


jokes = []
for j in jsonData:
    setup = j["setup"]
    punchLine = j["punchline"]
    joke = Joke(setup, punchLine)
    jokes.append(joke)

for joke in jokes:
    print(joke)
