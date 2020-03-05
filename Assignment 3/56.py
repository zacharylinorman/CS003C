######################################################
# Zachary Norman
# Input  - A string to count the vowels of
# Output - The number of vowels in the string
# Processing - The program counts the number of
#              vowels in the string and outputs it
######################################################

##########
# DRIVER #
##########
def main():
    # Input
    string = input("Enter a string: ")

    # Output
    print("Number of vowels: ", countVowels(string))

#############
# FUNCTIONS #
#############
def countVowels(string):
    """
    Counts the number of vowels in the given string
    :param string: The string to count the vowels of
    :return: The integer number of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

main()
