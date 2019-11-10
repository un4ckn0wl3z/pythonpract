friends = [
    {
        "name": "Anuwat",
        "location": "Nakhon Si Thammarat"
    },
    {
        "name": "Pansa",
        "location": "Chonburi"
    },
    {
        "name": "Surachad",
        "location": "Phattalung"
    },
    {
        "name": "Chaiyapat",
        "location": "Phuket"
    }
]


your_location = input("Where are right now? ")
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print("You are not alone!")
"""
* 0, 0.0
* None,
* [], (), {}
* False
"""

if all([1,2,3,0,5,6]):
    print('True')
else:
    print('False')

