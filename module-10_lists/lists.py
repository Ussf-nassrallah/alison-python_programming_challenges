print("Hi, you can invite five friends to the party :)")

friends = []
count = 0

while count < 5:
    friend = str(input("Enter the guest's name: "))
    friends.append(friend)
    count += 1

friends.sort()

for index in range(0, count):
    print("F{}: {}".format(index + 1, friends[index]))

print("the date of the party: 18/8/2023 at 12:00AM.")