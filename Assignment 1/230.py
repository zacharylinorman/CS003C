######################################################
# Zachary Norman
# Input  - None
# Output - The Olympic Rings
# Processing - The program draws the Olympic rings
#              using ezgraphics
######################################################

###########
# Imports #
###########
from graphics import GraphicsWindow

#############
# Constants #
#############
CANVAS_WIDTH = 720
CANVAS_HEIGHT = 720
CIRCLE_DIAMETER = 100

#######################
# Processing & Output #
#######################
# Creating the window
win = GraphicsWindow(CANVAS_WIDTH, CANVAS_HEIGHT)
canvas = win.canvas()

# Setting the line size
canvas.setLineWidth(5)

# Drawing the rings
canvas.setOutline("blue")
canvas.drawOval(CANVAS_WIDTH / 2 - CIRCLE_DIAMETER, CANVAS_HEIGHT / 2 - CIRCLE_DIAMETER / 2,
                CIRCLE_DIAMETER, CIRCLE_DIAMETER)

canvas.setOutline("black")
canvas.drawOval(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 - CIRCLE_DIAMETER / 2, CIRCLE_DIAMETER, CIRCLE_DIAMETER)

canvas.setOutline("red")
canvas.drawOval(CANVAS_WIDTH / 2 + CIRCLE_DIAMETER, CANVAS_HEIGHT / 2 - CIRCLE_DIAMETER / 2,
                CIRCLE_DIAMETER, CIRCLE_DIAMETER)

canvas.setOutline("yellow")
canvas.drawOval(CANVAS_WIDTH / 2 - CIRCLE_DIAMETER / 2, CANVAS_HEIGHT / 2, CIRCLE_DIAMETER, CIRCLE_DIAMETER)

canvas.setOutline("green")
canvas.drawOval(CANVAS_WIDTH / 2 + CIRCLE_DIAMETER / 2, CANVAS_HEIGHT / 2, CIRCLE_DIAMETER, CIRCLE_DIAMETER)

win.wait()
