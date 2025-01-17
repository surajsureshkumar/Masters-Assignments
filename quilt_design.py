"""
This was one of my assignments for my bridge course at the start of masters

This is a program that draws quilt design along with
an own design for the third and final block whereas the design
for the first two blocks are pre-requisite.
"""

import turtle as t


def init():
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    t.setup(1.0, 1.0)
    t.up()
    t.setheading(0)
    t.showturtle()
    t.title('quilt_design')
    t.speed(0)


# This functions draws the border for one square
def square_border():
    """
        :pre: pos (0,0), heading (east), right
        :post: pos relative, heading (east), right
        :return: None
    """
    t.pendown()
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(200)
    t.pen()
    t.right(90)
    t.forward(160)
    t.right(90)
    t.forward(200)
    t.penup()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    t.forward(200)
    t.right(90)
    t.forward(160)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(200)
    t.right(180)
    t.penup()


# To move the turtle to the center of the block
def center_pos_turtle():
    """
            :pre: pos relative, heading (east), right
            :post: pos relative, heading (east), right
            :return: None
            """
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)


# Draws the big triangle for Block 1 in purple color
def triangle_block1():
    """
            :pre: pos relative, heading (east), right
            :post: pos relative, heading (north), up
            :return: None
            """
    t.color('purple')
    t.begin_fill()
    t.pendown()
    t.forward(50)
    t.left(135)
    t.forward(35)
    t.left(90)
    t.forward(35)
    t.end_fill()
    t.color('red')


def mini_triangle():
    """mini_triangle functions creates the triangle in between the triangles in purple
            :pre: pos relative, heading (east), right
            :post: pos relative, heading (east), right
            :return: None
            """
    t.color('red')
    t.begin_fill()
    t.forward(26)
    t.right(90)
    t.forward(25)
    t.right(135)
    t.forward(35)
    t.right(135)
    t.end_fill()
    t.color('black')



def block1_triangles():
    """block1_triangles function draws the remaining blocks for triangle_block1, contains two for loops where:
    First for loop iterates to build the 4 big triangles in purple
    Second for loop iterates to build the 4 small triangles in red
            :pre: pos relative, heading (east), right
            :post: pos relative, heading (east), right
            :return: None
            """
    for i in range(4):
        triangle_block1()
        t.right(135)

    for i in range(4):
        mini_triangle()
        t.left(90)


 
def block_two_triangles():
    """block_two_triangles function draws the triangle pattern for second block
            :pre: pos relative, heading (east), right
            :post: pos (50,50), heading (east), right
            :return: None
            """
    t.pendown()
    t.forward(55)
    t.left(135)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.end_fill()
    t.penup()
    t.forward(40)
    t.left(135)
    t.forward(27.5)
    t.left(180)
    t.penup()


def block_two_design():
    """block_two_design function uses the above functions to draw the pattern design for second block
            :pre: pos relative, heading (east), right
            :post: pos (50,50), heading (east), right
            :return: None
            """
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(180)

    # for loop for first pair triangles
    # iterates to create the first two triangles
    for i in range(2):
        t.pendown()
        t.color('orange')
        t.begin_fill()
        block_two_triangles()

    t.penup()

    # for loop for second pair triangles
    t.left(90)
    t.forward(55)
    t.right(180)
    for i in range(2):
        t.color('blue')
        t.begin_fill()
        block_two_triangles()
    t.left(90)
    t.penup()

    # for loop for third pair triangles
    t.forward(55)
    t.right(180)
    for i in range(2):
        t.color('maroon')
        t.begin_fill()
        block_two_triangles()
    t.penup()

    # for loop for fourth pair triangle
    t.left(90)
    t.forward(55)
    t.right(180)
    for i in range(2):
        t.color('black')
        t.begin_fill()
        block_two_triangles()
    t.penup()

    # The below two lines brings the turtle to the center of the screen and turns it right
    t.forward(50)
    t.right(90)


def block_three_design():
    """block_three_design functions draws the design inside the block three
            :pre: pos relative, heading (east), right
            :post: pos relative, heading (east), right
            :return: None
            """
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    # Below for loop creates the spiral by iterating through the colors to print multi-colors spiral
    for i in range(114):
        t.color(colors[i % 5])  # i%5 to change colors
        t.circle(2 + i / 2, 45)
    square_circle_block()
    t.pendown()
    t.penup()
    # The below lines of code moves the turtle to its relative position
    t.left(180)
    t.forward(101)
    t.right(90)
    t.forward(165)
    t.right(180)
    t.mainloop()


# The below function draws the square block around the circle which is used in the block_three_design
def square_circle_block():
    t.forward(57)
    t.left(90)
    t.forward(114.5)
    t.left(90)
    t.forward(114.5)
    t.left(90)
    t.forward(114.5)
    t.left(90)
    t.forward(57)


def main() -> None:
    """
    The main function.
    :pre: pos (0,0), heading (east), right
    :post: pos (0,0), heading (east), right
    :return: None
    """
    init()
    square_border()
    t.forward(250)
    square_border()
    t.left(180)
    t.forward(500)
    t.right(180)
    square_border()
    center_pos_turtle()
    block1_triangles()
    mini_triangle()
    t.penup()
    t.forward(250)
    block_two_design()
    t.forward(250)
    t.pendown()
    block_three_design()
    t.mainloop()


if __name__ == '__main__':
    main()
