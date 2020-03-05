######################################################
# Zachary Norman
# Input  - A string to reverse
# Output - The reversed string
# Processing - The program reverses a string and
#              outputs it
######################################################

##########
# DRIVER #
##########
def main():
    # Input
    string = input("Enter a string: ")

    # Output
    print(reverse(string))

#############
# FUNCTIONS #
#############
def reverse(string):
    """
    This functions reverses a string
    :param string: The string to reverse
    :return: The reversed string
    """

    # Base Case
    if len(string) == 1:
        return string

    # Recursive Call
    return reverse(string[1:]) + string[0]

main()
