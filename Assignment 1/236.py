######################################################
# Zachary Norman
# Input  - The initial balance
#        - The annual interest
# Output - The balance of each of the first three
#          months after the interest is compounded
# Processing - The program computes the monthly
#              compounded interest using the compound
#              interest formula
######################################################

#############
# Constants #
#############
PERCENT_TO_DECIMAL = 100
MONTHS_IN_A_YEAR = 12

#########
# Input #
#########
userInput = input("Initial balance: ")
balance = float(userInput)
userInput = input("Annual interest rate in percent: ")
interestRate = float(userInput)

#######################
# Processing + Output #
#######################
# Each interest compound is followed by outputting the resultant balance
balance += balance * ((interestRate / PERCENT_TO_DECIMAL) / MONTHS_IN_A_YEAR)
print("After first month:  %5.2f" %balance)

balance += balance * ((interestRate / PERCENT_TO_DECIMAL) / MONTHS_IN_A_YEAR)
print("After second month: %5.2f" % balance)

balance += balance * ((interestRate / PERCENT_TO_DECIMAL) / MONTHS_IN_A_YEAR)
print("After third month:  %5.2f" %balance)
