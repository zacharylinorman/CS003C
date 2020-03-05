######################################################
# Zachary Norman
# Input  - an x, y, and z value to compare
# Output - Comparisons using the three functions
# Processing - The program checks to see if the three
#              given values are all the same, all
#              different, and if they are sorted from
#              smallest to largest
######################################################

##########
# DRIVER #
##########
def main():
    # Input
    x = input("X: ")
    y = input("Y: ")
    z = input("Z: ")

    # Output
    print("All the same: ", allTheSame(x, y, z))
    print("All different: ", allDifferent(x, y, z))
    print("Sorted: ", sorted(x, y, z))

#############
# FUNCTIONS #
#############
def allTheSame(x, y, z):
    """
    Checks to see if all of the parameters are the same value
    :param x: first parameter
    :param y: second parameter
    :param z: third parameter
    :return: True if all parameters are equivalent in value, and False if otherwise
    """
    return x == y == z


def allDifferent(x, y, z):
    """
    Checks to see if all of the parameters have different values
    :param x: first parameter
    :param y: second parameter
    :param z: third parameter
    :return: True if all parameters have different values, and False if otherwise
    """
    return x != y != z


def sorted(x, y, z):
    """
    Checks to see if the parameters are sorted from smallest to largest
    :param x: first parameter
    :param y: second parameter
    :param z: third parameter
    :return: True if the parameters are sorted from smallest to largest, and False if otherwise
    """
    return x <= y <= z


main()
