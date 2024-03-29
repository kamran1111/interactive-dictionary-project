import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate (w):
    w = w.lower() #It will convert all input to lowercase
    #lowercase will help in tackling input mix case letters
    if w in data:
        return data[w]   #If match is found, it return the word
    elif w.title() in data:  #If user has entered "delhi or DELHI", this will check for "Delhi"
        return data[w.title()]
    elif w.upper() in data:  # in case user enters acronyms like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:   #If there are similar words, it will be returned
        yesno = input("Did you mean - %s - instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])   #Using first similar word from aboe step
        yesno = yesno.upper()  #capital or small case Yes [y] or No [N}
        if yesno == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yesno == "N":
            return "The word does not exist. Please double check it"
        else:
            return "We didn't understand the word you entered"
    else:
        return "The word does not exist. Please double check it"

word = input ("Enter word: ")

output= (translate (word))  #It is list of definitions

if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)