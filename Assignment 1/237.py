######################################################
# Zachary Norman
# Input  - The number of movie rentals
#        - The number of member referrals
# Output - The discount amount
# Processing - The program computes the discount
#              amount and checks to see if it is
#              under the maximum value
######################################################

#############
# Constants #
#############
MAXIMUM_DISCOUNT = 75.00

#########
# Input #
#########
userInput = input("Enter the number of movie rentals: ")
numMovieRentals = int(userInput)
userInput = input("Enter the number of members referred to the video club: ")
numReferrals = int(userInput)

##############
# Processing #
##############
discount = MAXIMUM_DISCOUNT
if numMovieRentals + numReferrals < MAXIMUM_DISCOUNT:
    discount = numMovieRentals + numReferrals

##########
# Output #
##########
print("The discount is equal to: %5.2f" % discount, " percent.")
