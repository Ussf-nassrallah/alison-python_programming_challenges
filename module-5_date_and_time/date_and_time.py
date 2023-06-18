import datetime

currentDay = datetime.date.today()

# print full current year + month + day
# print(currentDay)
# print current year
# print(currentDay.year)
# print current month
# print(currentDay.month)
# print current day
# print(currentDay.day)

# strftime allows you to specify the date format
# d: day, b: month name, Y: year, y: 2 Digits year
# print(currentDay.strftime("%d %b %y"))

# please attend our event Sunday, July 20 in the year 1997
# print(currentDay.strftime('please attend our event %A, %B %d in the year %Y'))

userInput = input("Hey, Please Enter your birthday (mm/dd/yyyy): ")
userBirthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
days = userBirthday - currentDay
print(days)