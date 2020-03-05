###################################################
# Zachary Norman
# Input  - The value of the bill inserted
#        - The value of the purchased item
# Output - The number of dollar coins
#        - The number of quarters
# Processing - The program calculates the change
#              in terms of number of dollar coins
#              and quarters
###################################################
# Constants
PENNIES_IN_A_DOLLAR = 100
PENNIES_IN_A_QUARTER = 25

# Input
userInput = input("Enter bill value (1 = $1 bill, 5 = $5 bill, etc.): ")
billInserted = float(userInput)
userInput = input("Enter item price (4.25 = $4.25, 3.00 = $3.00, etc.: ")
itemPrice = float(userInput)

# Computations
change = (billInserted - itemPrice) * PENNIES_IN_A_DOLLAR
numDollarCoins = int(change // PENNIES_IN_A_DOLLAR)
numQuarters = int((change - numDollarCoins * PENNIES_IN_A_DOLLAR) // PENNIES_IN_A_QUARTER)

# Output
print("Number of dollar coins: %6d" % numDollarCoins)
print("Number of quarters:     %6d" % numQuarters)
