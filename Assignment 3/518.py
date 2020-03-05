######################################################
# Zachary Norman
# Input  - An integer to count the digits of
# Output - The number of digits in the integer
# Processing - The program counts the number of
#              digits in the given integer
######################################################

##########
# DRIVER #
##########
def main():
    # Input
    num = int(input("Enter an integer: "))

    # Output
    print(numDigits(num))

#############
# FUNCTIONS #
#############
def numDigits(n):
    """
    This functions counts the number of digits in an integer
    :param n: The integer to count the number of digits of
    :return: The integer number of digits in the given integer
    """

    # Base Case
    if n < 10:
        return 1

    # Recursive Call
    return 1 + numDigits(n // 10)

main()
