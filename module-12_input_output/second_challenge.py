import csv

fileName = "users.txt"

with open(fileName, 'r') as file:
    users = csv.reader(file)
    for user in users:
        print(', '.join(user))