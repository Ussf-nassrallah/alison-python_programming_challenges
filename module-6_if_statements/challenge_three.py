total = 0
shipping_cost = 10
free_shipping = False
customer = input("Please Enter Your name: ")
amount = int(input("Enter the amount for your total purchase: "))

if amount > 50:
    free_shipping = True
    total = amount
    print("congratulations, {}, Shipping is free.".format(customer))
    print("Your Total is : ${}".format(total))
else:
    total = amount + shipping_cost
    print("Thanks, {} for taking this action".format(customer))
    print("Your amount is : ${}".format(amount))
    print("Shopping cost is : ${}".format(shipping_cost))
    print("Your Total is : ${}".format(total))

print("Thanks, {}.\nhave a good day.".format(customer))