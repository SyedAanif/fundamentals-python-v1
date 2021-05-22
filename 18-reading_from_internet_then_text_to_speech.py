# BEFORE RUNNING text-to-speech, DO pip3 install pyttsx3
# READING FROM INTERNET
import requests
# FETCHING JSON FORMAT FROM INTERNET
import json
# TEXT TO SPEECH
import pyttsx3

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
        return f"Setup = {self.setup}, PunchLine = {self.punchLine}"


jokes = []
for j in jsonData:
    setup = j["setup"]
    punchLine = j["punchline"]
    joke = Joke(setup, punchLine)
    jokes.append(joke)

print(f"Got {len(jokes)} Jokes")
# MAKING THE LIBRARY SPEAK
pyttsx3.speak("Hello. You can now convert text to speech")

for joke in jokes:
    print(joke)
    pyttsx3.speak(joke.setup)
    pyttsx3.speak(joke.punchLine)
