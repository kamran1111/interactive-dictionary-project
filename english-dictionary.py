import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate (w):
    w = w.lower() #It will convert all input to lowercase
    #lowercase will help in tackling input mix case letters
    if w in data:
        return data[w]   #If match is found, it return the word
    elif len(get_close_matches(w, data.keys())) > 0:   #If there are similar words, it will be returned
        yesno = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])   #Using first similar word from aboe step
        if yesno =="Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
    else:
        return "The word does not exist. Please double check it"

word = input ("Enter word: ")

print (translate (word))