######################################################
# Zachary Norman
# Input  - The problem to be tested
#        - The string to be modified
# Output - The modified string
# Processing - The program compacts  the 5 different
#              problems of P4.3 into one sentinel-
#              controlled program. It modifies a
#              given string based on which problem
#              the user selects using loops.
######################################################

#############
# Constants #
#############
VOWELS = "aeiou"
PROBLEM_SET = "abcde"

##############
# Processing #
##############
# Initial problem selection
problem = input("Which program would you like to run? (Enter: a, b, c, d, or e) ")

# Main while loop
while problem != "":

    # Check if valid problem selection
    if len(problem) == 1 and problem in PROBLEM_SET :

        # User input of string to modify
        string = input("Enter a string: ")

        # String to output
        output = ""

        #############
        # PROBLEM A #
        #############
        if problem == "a":
            # Loop through each letter and check if it is uppercase
            for letter in string:
                if letter.isupper():
                    output += letter
        #############
        # PROBLEM B #
        #############
        elif problem == "b":
            # Split the string into a list of words
            words = string.split(" ")

            # Add each of the second letters of the words to the output
            for word in words:
                output += word[1] if len(word) > 1 else ""


        #############
        # PROBLEM C #
        #############
        elif problem == "c":
            for letter in string:
                # If the letter is not a vowel add it to the output,
                # otherwise add an underscore
                output += letter if letter not in VOWELS else "_"

        #############
        # PROBLEM D #
        #############
        elif problem == "d":
            # Create a variable to count the number of digits
            count = 0

            # Count the number of digits in the string
            for letter in string:
                if letter.isdigit():
                    count += 1

            # Change the count to a string to ready it for output
            output = str(count)

        #############
        # PROBLEM E #
        #############
        elif problem == "e":
            # Create a variable that holds the length of the string
            stringLength = len(string)

            # Loop through each letter of the string using an index
            for i in range(stringLength):
                # If the letter is is a vowel, add its position to the output
                if string[i] in VOWELS:
                    output += str(i + 1) + ", "

            # Remove the last ', ' from the output
            output = output[:-2]

        # Print the output
        print(output)

    # If not valid problem input, output an error message
    else:
        print("Error: Please enter a valid problem.")

    # Ask for next problem, or enter to exit
    print() # Output a new line first
    problem = input("Which program would you like to run? (Press Enter to exit) ")

# A nice good bye message :)
print("Good Bye!")
