import json
from difflib import get_close_matches
data = json.load(open("original/data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean {} instead? type Y if yes, type N if no: ".format(get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return " The word doesn't exit please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "This word doesn't exit. Please cross check it."

word = input("Type a word: ")
print (translate(word))
