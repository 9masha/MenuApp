import json


def load(fileName):
    try:
        file = open(f"./{fileName}.json", "r")
        data = json.loads(file.read())
        return data
    except:
        print("The file was not found")

