#####################################################
# Zachary Norman
# Input  - Two times in military format
# Output - The number of hours and minutes apart
# Processing - The program calculates the difference
#              in time between two given times in
#              military format
#####################################################

#############
# Constants #
#############
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24
HOUR_MINUTE_SEPARATION = 100

#########
# Input #
#########
userInput = input("Input the first time: ")
firstTime = int(userInput)
userInput = input("Input the second time: ")
secondTime = int(userInput)

##############
# Processing #
##############
# Convert to minutes
firstTime = (MINUTES_IN_AN_HOUR * (firstTime // HOUR_MINUTE_SEPARATION)) + (firstTime % HOUR_MINUTE_SEPARATION)
secondTime = (MINUTES_IN_AN_HOUR * (secondTime // HOUR_MINUTE_SEPARATION)) + (secondTime % HOUR_MINUTE_SEPARATION)

# Check if second time is next day and handle if it is
if secondTime < firstTime:
    secondTime += HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR

# Compute minutes in between
minutesInBetween = abs(firstTime - secondTime)

# Find the number of hours and number of minutes
numHours = minutesInBetween // MINUTES_IN_AN_HOUR
numMinutes = minutesInBetween - numHours * MINUTES_IN_AN_HOUR

##########
# Output #
##########
print(numHours, " hours ", numMinutes, " minutes ")
