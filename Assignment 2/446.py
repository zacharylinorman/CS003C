######################################################
# Zachary Norman
# Input  - No user input, but an image must be
#          provided to be modified
# Output - The modified image
# Processing - The program increases the red level of
#              each pixel of the given image by 30%
#              up to 255 then draws both images for
#              a side by side comparison
######################################################

###########
# Imports #
###########
from graphics import GraphicsImage, GraphicsWindow

#############
# Constants #
#############
CANVAS_WIDTH = 1024
CANVAS_HEIGHT = 450
RGB_MAX = 255
RED_MULTIPLIER = 1.3
FILENAME = "image.PNG"

# Window Creation
win = GraphicsWindow(CANVAS_WIDTH, CANVAS_HEIGHT)
canvas = win.canvas()

# Create a variable for the original image
image = GraphicsImage(FILENAME)

# Copy the image over to a new placeholder to modify
newImage = image.copy()
width = newImage.width()
height = newImage.height()

##############
# PROCESSING #
##############
# Loop through each pixel to modify its red level
for row in range(height):
    for col in range(width):
        # Obtain the current RGB levels of the pixel
        red = newImage.getRed(row, col)
        green = newImage.getGreen(row, col)
        blue = newImage.getBlue(row, col)

        # Create a new red that is 30% greater with a max of 255
        newRed = int(red * RED_MULTIPLIER if red * RED_MULTIPLIER < RGB_MAX else RGB_MAX)

        # Replace the pixel with the updated RGB values
        newImage.setPixel(row, col, newRed, green, blue)

# Save the altered image
newImage.save("sunset_" + FILENAME)

# Draw the original and modified images to the window
canvas.drawText(0, 0, "Before: ")
canvas.drawText(width, 0, "After: ")
canvas.drawImage(0, 16, image)
canvas.drawImage(width, 16, newImage)

win.wait()
