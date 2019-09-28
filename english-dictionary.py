import json

data = json.load(open("data.json"))

def translate (w):
    w = w.lower() #It will convert all input to lowercase
    #lowercase will help in tackling input mix case letters
    if w in data:
        return [w]
    else:
        return "The word does not exist. Please double check it"

word = input ("Enter word: ")

print (translate (word))