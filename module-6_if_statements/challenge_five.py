country = input("where are you from ? : ").lower()
total = 100
target = "canada"

if country == target.lower():
    province = input("which province ? : ").lower()
    if province == "alberta":
        total = total + (total * 0.05)
    elif province == "ontario" or province == "new brunswick"\
            or province == "nova scotia" or province == "harmonized":
        total = total + (total * 0.13)
    else:
        total = total + (total * 0.06)
    print("Your total is ${}".format(total))
else:
    print("Customer comes from another country. total is ${}".format(total))