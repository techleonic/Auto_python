import json


file = open("data.json")
data =  json.load(file)


def define(word):
    if word in data:
        return data[word]


word = input("enter a word: ")
definition = define(word.lower())
if definition:
    for item in definition:
        print(item)
else:
    print("not found")