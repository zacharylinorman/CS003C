######################################################
# Zachary Norman
# Input  - A string is initialized within the program
# Output - The first three characters followed by
#          three periods followed by the last three
#          characters of the string
# Processing - The program creates an altered version
#              of an initialized string using
#              character indexes of strings as well
#              as string concatenation
######################################################

#############
# Constants #
#############
TRIPLE_DOTS = "..."

##############
# Processing #
##############
stringVariable = "Zachary Li Norman"
stringLength = len(stringVariable)

firstThree = stringVariable[0] + stringVariable[1] + stringVariable[2]
lastThree = stringVariable[stringLength - 3] + stringVariable[stringLength - 2] + stringVariable[stringLength - 1]

alteredString = firstThree + TRIPLE_DOTS + lastThree

##########
# Output #
##########
print("The original string is: ", stringVariable, ", the altered string is: ", alteredString)
