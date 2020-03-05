######################################################
# Zachary Norman
# Input  - The program defines two lists of integers
# Output - Whether the two lists are the same set
# Processing - The program iterates through a list to
#              check if it is the same set as the
#              other list
######################################################

##########
# DRIVER #
##########
def main():

    # Input
    a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    b = [11, 11, 7, 9, 16, 4, 11]

    # Output
    print("The lists %s and %s are the same set: %s" %(a, b, sameSet(a, b)))
    return


#############
# FUNCTIONS #
#############
def sameSet(a, b):
    """
    Checks if the two given lists are the same set
    :param a: The first list
    :param b: The second list
    :return: True if the lists are the same set, Flase if otherwise
    """

    # Iterate through the longer list
    for value in (a if len(a) > len(b) else b):

        # If the value is not in the other list, they are not the same set
        if value not in (b if len(a) > len(b) else a):
            return False

    # All checks passed!
    return True


main()
