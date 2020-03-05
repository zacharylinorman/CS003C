##
# P4.46 Implement a “sunset” effect by increasing the red level of each pixel
#   of an image by 30 percent (up to a value of 255).
#

from graphics import GraphicsWindow, GraphicsImage

# input
image_name = input("Please put your image file with this module together in same location and enter the name of your image file (image.jpg): ")

win = GraphicsWindow()
# initialization
oriImage = GraphicsImage(image_name)
width = oriImage.width()
height = oriImage.height()
newImage = GraphicsImage(width, height)

# calculation
for row in range(height):
    for col in range(width):
        red = oriImage.getRed(row, col)
        green = oriImage.getGreen(row,col)
        blue = oriImage.getBlue(row, col)

        newRed = int(red*1.3)
        if newRed == 0:
            newRed += 30
        if newRed > 255:
            newRed = 255

        newImage.setPixel(row, col, newRed, green, blue)
# output
canvas = win.canvas()
canvas.drawImage(newImage)

newImage.save("Redder-" + image_name + ".gif")
win.wait()

# save


##
# sample run
#   None