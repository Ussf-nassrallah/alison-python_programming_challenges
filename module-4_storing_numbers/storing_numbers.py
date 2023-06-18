"""
Challenge: create a loan calculator.
Input:
    Have the user enter
        - the cost of the loan
        - the interest rate
        - the number of years for the loan
Output:
    Calculate monthly payments with the following formula
        output = L[i(1 + i)n] / [(1 + i)n-1]
"""

# Declare and initialize the variables
monthlyPayment = 0
loanAmount = 0
interestRate = 0
numberOfPayments = 0
loanDurationInYears = 0

# Ask the user for the values needed to calculate the monthly payments
strLoanAmount = input("How much money will you borrow? ")
strInterestRate = input("What is the interest rate on the loan? ")
strLoanDurationInYears = input("How many years will it take you to pay off the loan? " )

# Convert the strings into floating numbers so we can use them in teh formula
loanDurationInYears = float(strLoanDurationInYears)
loanAmount = float(strLoanAmount)
interestRate = float(strInterestRate)

# Since payments are once per month, number of payments is number of years for the loan * 12
numberOfPayments = loanDurationInYears*12

# Calculate the monthly payment based on the formula
monthlyPayment = loanAmount * interestRate * (1+ interestRate) * numberOfPayments \
    / ((1 + interestRate) * numberOfPayments -1)

# provide the result to the user
print("Your monthly payment will be " + str(monthlyPayment))

# Extra credit
print("Your monthly payment will be $%.2f" % monthlyPayment)