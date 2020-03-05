######################################################
# Zachary Norman
# Input  - A list of integers
# Output - The alternating sum of the list
# Processing - The program adds add the odd indexes
#              and subtracts all the even indexes
######################################################

##########
# DRIVER #
##########
def main():

    # Input
    myList = []
    userInput = input("Enter integer to add to list, or Enter to stop: ")
    while userInput != "":
        myList.append(int(userInput))
        userInput = input("Enter integer to add to list, or Enter to stop: ")

    # Output
    print("The alternating sum is: ", alternatingSum(myList))
    return

#############
# FUNCTIONS #
#############
def alternatingSum(myList):
    """
    Calculates and returns the alternating sum of the given list of integers
    :param myList: A list of integers
    :return: The alternating sum of the list
    """

    # Add the indexes 0, 2, 4, ..., 2n and subtract indexes 1, 3, 5, ..., 2n + 1
    return sum(myList[::2]) - sum(myList[1::2])


main()

