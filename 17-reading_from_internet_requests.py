# BEFORE RUNNING requests, DO pip3 install requests
# READING FROM INTERNET
import requests
# FETCHING JSON FORMAT FROM INTERNET
import json

url = "http://official-joke-api.appspot.com/random_ten"
response = requests.get(url)
print(response.status_code)
data = response.text
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
