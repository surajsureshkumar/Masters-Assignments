from turtle import Turtle

from mobile_node import Node


class Ball(Node):
    __slots__ = "name", "cord_length", "radius", "weight"

    def __init__(self, name, cord_length, radius, weight):
        """
        Constructor
        :param name: ball name
        :param cord_length: cord length
        :param radius: radius of the ball
        :param weight: weight of the ball
        """
        super().__init__(name, cord_length)
        self.radius = radius
        self.weight = weight

    def __str__(self):
        """
        String representation
        :return: String
        """
        return f'Ball(name = {self.get_name()}, cord = {self.cord_length}, radius = {self.radius}, ' \
               f'weight = {self.weight}'

    def get_weight(self) -> int:
        """
        Get the node's weight
        :return: the weight
        """
        return self.weight

    def get_height(self) -> int:
        """
        Get the node's height
        :return: the height
        """
        return self.cord_length + (2 * self.radius)

    def get_width(self) -> int:
        """
        Get the total node's width
        :return: the total width
        """
        return self.get_right_width() + self.get_left_width()

    def get_left_width(self) -> int:
        """
        Get the total width of the left child
        :return: the left width
        """
        return self.radius

    def get_right_width(self) -> int:
        """
        Get the total width of the right child
        :return: the right width
        """
        return self.radius

    def is_balanced(self) -> bool:
        """
        Whether the node is balanced
        :return:
        """
        return True

    def get_imbalance(self):
        """
        Get the node's amount of imbalance.
        Imbalance is the different between its left and right torques.
        :return: the node's imbalance.
        """
        return 0

    def infix(self) -> str:
        """
        Get a infix string representation of the node
        :return: the infix string
        """
        return "( " + self.get_name() + ' )'

    def print_pretty(self, tabs: str) -> str:
        """
        Get a preorder string representation of the node
        :param tabs: the indentation level
        :return: the preorder string
        """
        return tabs + self.get_name()

    def write_on_side(self, t, text, direction):
        """
         Writes the text on the sides of the ball
        :param t: turtle
        :param text: is the text to be displayed
        :param direction: is the direction for the turtle to move
        :return: None
        """
        # writes the text to the right of the ball
        if direction == 'right':
            t.penup()
            t.forward(10)
            t.pendown()
            t.color('red')
            t.write(text)
            t.color('green')
            t.penup()
            t.back(10)
        # writes the text to the below the ball
        elif direction == 'down':
            t.penup()
            t.right(90)
            t.forward(self.radius + 15)
            t.left(90)
            t.back(20)
            t.write(text)
            t.penup()
            t.forward(20)
            t.left(90)
            t.forward(self.radius + 15)
            t.right(90)
            t.pendown()

    def draw(self, t: Turtle) -> None:
        """
        Draw the node using Turtle.
        :pre: pen down, facing south, position: top of the node's cord
        :post: pen down, facing south, position: top of the node's cord
        :param t: the turtle's instance
        :return: None
        """
        t.color('green')
        t.forward(self.cord_length)
        t.right(90)
        t.circle(self.radius)
        t.penup()
        t.left(90)
        t.forward(self.radius)
        t.left(90)
        t.pendown()
        t.forward(self.radius)
        self.write_on_side(t, 'W' + str(self.weight), 'right')
        t.back(self.radius)
        self.write_on_side(t, self.get_name(), 'down')
        t.left(90)
        t.penup()
        t.forward(3)
        t.right(90)
        t.pendown()
        t.write(self.radius)
        t.penup()
        t.left(90)
        t.forward(self.radius + self.cord_length - 3)
        t.left(180)
        t.color('black')
        t.down()

    def find(self, name: str) -> 'Node':
        """
        Find a node by name
        :param name: the node's name
        :return: the node or None
        """
        if name == self.get_name():
            return self
