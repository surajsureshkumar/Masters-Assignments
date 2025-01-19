from turtle import Turtle

from mobile_node import Node


class Rod(Node):
    __slots__ = "name", "cord_length", "left_arm_length", "left_child", "right_arm_length", "right_child"

    def __init__(self, name, cord_length, left_arm_length, left_child: Node or None, right_arm_length,
                 right_child: Node or None):
        """
        Constructor
        :param name: rod name
        :param cord_length: the cord length
        :param left_arm_length: left arm length
        :param left_child: left child of the left arm
        :param right_arm_length: right arm length
        :param right_child: right child of the right arm
        """
        super().__init__(name, cord_length)
        self.left_arm_length = left_arm_length
        self.left_child = left_child
        self.right_arm_length = right_arm_length
        self.right_child = right_child

    def __str__(self):
        """
        String representation
        :return: String
        """
        return f'Rod( name = {self.get_name()}, cord = {self.cord_length},  leftChild = {self.left_child}, ' \
               f'rightArm = {self.right_arm_length},rightChild = {self.right_child}'

    def get_weight(self) -> int:
        """
        Get the node's weight
        :return: the weight
        """
        return self.left_child.get_weight() + self.right_child.get_weight()

    def get_height(self) -> int:
        """
        Get the node's height
        :return: the height
        """
        return self.cord_length + max(self.right_child.get_height(), self.left_child.get_height())

    def get_width(self) -> int:
        """
        Get the total node's width
        :return: the total width
        """
        return self.get_left_width() + self.get_right_width()

    def get_left_width(self) -> int:
        """
        Get the total width of the left child
        :return: the left width
        """
        immediate_left_width = self.left_arm_length + self.left_child.get_left_width()
        right_child_left_width = self.right_child.get_left_width() - self.right_arm_length
        return max(immediate_left_width, right_child_left_width)

    def get_right_width(self) -> int:
        """
        Get the total width of the right child
        :return: the right width
        """
        immediate_right_width = self.right_arm_length + self.right_child.get_right_width()
        left_child_right_width = self.left_child.get_right_width() - self.left_arm_length
        return max(immediate_right_width, left_child_right_width)

    def is_balanced(self) -> bool:
        """
        Whether the node is balanced
        :return:
        """
        return self.get_imbalance() == 0

    def get_imbalance(self):
        """
        Get the node's amount of imbalance.
        Imbalance is the different between its left and right torques.
        :return: the node's imbalance.
        """

        return abs(self.left_arm_length * self.left_child.get_weight() -
                   self.right_arm_length * self.right_child.get_weight())

    def infix(self) -> str:
        """
        Get a infix string representation of the node
        :return: the infix string
        """
        return '(' + self.left_child.infix() + ' ' + self.get_name() + ' ' + self.right_child.infix() + ')'

    def print_pretty(self, tabs: str) -> str:
        """
        Get a preorder string representation of the node
        :param tabs: the indentation level
        :return: the preorder string
        """
        return tabs + self.get_name() + '\n' + self.left_child.print_pretty(tabs + '\t') + \
               '\n' + self.right_child.print_pretty(tabs + '\t')

    def write_on_side(self, t, text, direction):
        """
        Writes the text on the sides of the Rod
        :param t: turtle
        :param text: is the text to be displayed
        :param direction: is the direction for the turtle to move
        :return: None
        """
        # writes the text to the right of the rod
        if direction == 'right':
            t.forward(10)
            t.write(text)
            t.back(10)
        # writes the text to the left of the rod
        elif direction == 'left':
            t.back(50)
            t.write(text)
            t.forward(50)
        # writes the text to the up right of the rod
        elif direction == 'up-right':
            t.penup()
            t.right(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.right(90)
            t.color('red')
            t.pendown()
            t.write(text)
            t.penup()
            t.color('black')
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.down()
        # writes the text to the up left of the rod
        elif direction == 'up-left':
            t.penup()
            t.right(180)
            t.forward(10)
            t.right(90)
            t.color('red')
            t.pendown()
            t.write(text)
            t.penup()
            t.color('black')
            t.right(90)
            t.forward(10)
            # t.left(90)
            # t.forward(10)
            # t.right(90)
            t.down()

    def draw(self, t: Turtle) -> None:
        """
        Draw the node using Turtle.
        :pre: pen down, facing south, position: top of the node's cord
        :post: pen down, facing south, position: top of the node's cord
        :param t: the turtle's instance
        :return: None
        """
        t.pendown()
        t.forward(self.cord_length / 2)
        t.penup()
        t.left(90)
        self.write_on_side(t, self.cord_length, 'right')
        self.write_on_side(t, self.get_name(), 'left')
        # t.forward(3)
        # t.write(self.cord_length)
        # t.back(3)
        t.pendown()
        t.right(90)
        # t.left(90)
        t.forward(self.cord_length / 2)
        t.left(90)
        t.forward(self.right_arm_length)
        t.right(90)
        self.write_on_side(t, 'L' + str(self.right_arm_length), 'up-right')
        self.right_child.draw(t)
        t.right(90)
        t.forward(self.right_arm_length)
        t.forward(self.left_arm_length)
        t.left(90)
        self.write_on_side(t, 'L' + str(self.left_arm_length), 'up-left')
        self.left_child.draw(t)
        t.left(90)
        t.forward(self.left_arm_length)
        t.left(90)
        t.forward(self.cord_length)
        t.right(180)
        return

    def find(self, name: str) -> 'Node':
        """
        Find a node by name
        :param name: the node's name
        :return: the node or None
        """
        if name == self.get_name():
            return self
        else:
            return self.left_child.find(name) or self.right_child.find(name)
