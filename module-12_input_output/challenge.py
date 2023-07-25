
# create the CSV file
filename = "demo.csv"

users = [
    {"name": "youssef", "age": 23},
    {"name": "yassin", "age": 19},
    {"name": "iliass", "age": 24},
    {"name": "yahya", "age": 24},
]

with open(filename, 'w') as file:
    for user in users:
        file.write("{}, {}\n".format(user["name"], user["age"]))

file.close()

print("File written successfully")
