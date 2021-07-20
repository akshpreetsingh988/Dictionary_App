import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    # my dataset contains only letters in the lower case
    word = word.lower()
    if word in data:
        return data[word]
    elif len (get_close_matches(word,data.keys())) > 0:
        y_n =  input("Did you mean %s instead , Enter y if YES and n if NO" %get_close_matches(word,data.keys())[0])
        if y_n == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif y_n == "n":
            return "The Word you have entered does not exit , please double check it !"
        else:
            return "We did not understand your entry ."
    else :
        return "The word you have entered is not in the dictionary , please double check it !"

word = input("Enter the word -> ")

print(translate(word))