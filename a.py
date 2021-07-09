import json
from difflib import get_close_matches


data = json.load(open("original/data.json"))
user = input("Enter word: ").lower()

def dicti(user):
    if user in data:
        return data[user]
    elif user.capitalize() in data.keys():
        return data[user.capitalize()]
    elif user.upper() in data.keys():
        return data[user.upper()]      
    elif len(get_close_matches(user, data.keys()))>0:
        yn = (input("Did you mean {} instead? Enter Y if yes or N if no: ".format(get_close_matches(user, data.keys())[0]))).upper()
        if yn == "Y":
            return data[get_close_matches(user, data.keys())[0]]
        elif yn == "N":
            return "The word doen't exit, please double check it"
        else:
            return "We didnt understand your entry."
    else:
        return "The word doen't exit, please double check it"

output = dicti(user)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
