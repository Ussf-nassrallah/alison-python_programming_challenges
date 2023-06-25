sport = input("Enter your favorite sport : ").upper()
team = input("Enter your favorite hockey team : ").upper()

# if the sport is hockey, and the team is the senators or leafs, display the cub message
sportIsHockey = False
if sport == "hockey".upper():
    sportIsHockey = True

teamIsCorrect = False
if team == "senators".upper() or team == "leafs".upper():
    teamIsCorrect = True

if sportIsHockey and teamIsCorrect:
    print("Good luck getting to the cup this year")
