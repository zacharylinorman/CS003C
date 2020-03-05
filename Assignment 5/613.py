######################################################
# Zachary Norman
# Input  - The program defines two lists
# Output - Whether the two lists have the same
#          elements
# Processing - The program iterates through the two
#              sorted lists to check if they contain
#              the same elements
######################################################

##########
# DRIVER #
##########
def main():
    # Input
    a = [1, 2, 3]
    b = [3, 2, 1]

    # Output
    print("The lists %s and %s have the same elements: %s" %(a, b, sameElements(a, b)))
    return


#############
# FUNCTIONS #
#############
def sameElements(a, b):

    # First check to see if they are the same length
    if len(a) != len(b):
        return False

    # Create a copy of the second list
    b1 = b[:]

    # Iterate through th first list
    for value in a:
        if value not in b1:
            return False
        else:
            # If the value is in the second list, remove it
            b1.remove(value)

    return True

main()

#################################
# ALTERNATE SOLUTION USING SORT #
#################################
#   # First check to see if they are the same length
#   if len(a) != len(b):
#       return False
#
#   # Create a copy of each list
#   a1 = a[:]
#   b1 = b[:]
#
#   # Sort the two new lists
#   a1.sort()
#   b1.sort()
#
#   # Iterate through each of them to check if elements match
#   for i in range(len(a1)):
#       if a1[i] != b1[i]:
#           return False
#   return True

