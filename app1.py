
import json
import difflib
from difflib import get_close_matches

#openingn json file
data = json.load(open("data.json"))

#code that compares input with the definition base
def define(word):
    if word in data:
        return data[word]
    else: 
        try:
            if len(get_close_matches(word, data.keys())) > 0:
                yn =  input("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
                if yn == "Y":
                    return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
                else:
                    return("There is no such word in our database")
        except:
            message = "The word {} does not exist! Please retype it"
            return(message.format(word))

#Inputting your word here
word = input("Enter your word: ")


#error message in case word does not exist
out = define(word)
if type(out) == list:
    #loop for printing list items seperately
    for item in out:
        print(item)
else:
    #Printing error messages in one line
    print(out)

