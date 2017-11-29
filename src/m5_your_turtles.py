"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Rachel Wood.
"""
########################################################################
# DONE 1
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

# turtle_1 = rg.SimpleTurtle('turtle')
# turtle_1 .pen = rg.Pen('midnight blue', 3)
# turtle_1 .speed = 10  # Fast
# size=80

colors = ["red", "orange", "yellow", "green", "blue", "violet", "red"]

for k in range(6):
    turtle_1 = rg.SimpleTurtle('turtle')
    turtle_1.paint_bucket = rg.PaintBucket(colors[k])

    turtle_1.pen = rg.Pen(colors[k + 1], 3)
    turtle_1.speed = 10  # Fast

    turtle_1.begin_fill()

    turtle_1.left(60 * k)
    turtle_1.draw_square(180)

    turtle_1.end_fill()
    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    turtle_1.pen_down()
    # size = size + 20

colors = ["red", "orange", "yellow", "green", "blue", "violet", "red"]

for k in range(6):
    turtle_2 = rg.SimpleTurtle('turtle')
    turtle_2.paint_bucket = rg.PaintBucket(colors[k])

    turtle_2.pen = rg.Pen(colors[k + 1], 3)
    turtle_2.speed = 10  # Fast

    turtle_2.begin_fill()

    turtle_2.left(60 * k + 30)
    turtle_2.draw_square(90)

    turtle_2.end_fill()
    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    turtle_2.pen_down()
    # size = size + 20

colors = ["red", "orange", "yellow", "green", "blue", "violet", "red", "orange", "yellow", "green", "blue", "violet",
          "red"]

turtle_3 = rg.SimpleTurtle('turtle')
turtle_3.paint_bucket = rg.PaintBucket(colors[k])

turtle_3.pen = rg.Pen(colors[k + 1], 3)
turtle_3.speed = 10  # Fast
turtle_3.pen_up()
turtle_3.left(90)
turtle_3.forward(50)
turtle_3.right(90)
turtle_3.forward(10)
# turtle_3.left(90)
# turtle_3.forward(40)
# turtle_3.left(180)
turtle_3.pen_down()

for k in range(12):
    turtle_3.paint_bucket = rg.PaintBucket(colors[k])

    turtle_3.pen = rg.Pen(colors[k + 1], 3)
    turtle_3.speed = 10  # Fast

    turtle_3.begin_fill()

    turtle_3.draw_circle(10)

    turtle_3.end_fill()
    # Put the pen down again (so drawing resumes).
    turtle_3.pen_down()

    turtle_3.pen_up()
    turtle_3.right(30)
    turtle_3.forward(30)
    turtle_3.pen_down()

window.close_on_mouse_click()
