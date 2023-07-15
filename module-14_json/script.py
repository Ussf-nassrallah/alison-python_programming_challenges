import json

person = {
    "name": "John",
    "age": 23,
    "city": "New york",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

# conver python dict to a json object
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
print("----")

# conver json object to a python dict
person_b = json.loads(personJSON)
print(person_b)
print("----")

# dump it into a file
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

with open("person.json", "r") as file:
    person = json.load(file)
    print(person)
    print("----")

