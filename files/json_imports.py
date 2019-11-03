import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)

print(file_contents['friends'][0])

cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"}
]

with open('cars.json', 'w') as file:
    json.dump(cars, file)