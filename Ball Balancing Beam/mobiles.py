"""
This is a homework program that draws the mobile for the given
input file and displays its features
"""

import sys
from rod import Rod
from ball import Ball
import turtle as t


class Mobile:
    __slots__ = "filename", "node_data", "index", "root"

    def __init__(self, filename):
        """
        The constructor of Mobile class
        :param filename: the name of the file taken as input
        """
        self.filename = filename
        self.node_data = []
        self.index = 0
        self.root = None  # initializing root to None

    def turtle_init(self):
        """
        Initialize for drawing
        :return: returns t
        """
        t.setup(1.0, 1.0)
        t.up()
        t.setheading(0)
        t.showturtle()
        t.title('Mobile')
        t.speed(0)
        t.left(90)
        # mobile cord is going to start from the screen top
        t.setup(self.root.get_width() + 100, self.root.get_height() + 100)
        t.forward(self.root.get_height() / 2 + 50)
        t.right(90)
        # adjusting the left and right width of the screen
        # if left width is greater than right width then we are gonna subtract left width and right width and
        # divide it by 2 and move forward or else move back
        if self.root.get_left_width() > self.root.get_right_width():
            t.forward((self.root.get_left_width() - self.root.get_right_width()) / 2)
        elif self.root.get_left_width() < self.root.get_right_width():
            t.back((-self.root.get_left_width() + self.root.get_right_width()) / 2)
        return t

    def help(self) -> str:
        """
        Help functions is used to display the user the list of available commands to execute
        :return: A string of commands
        """
        return '"quit": end the program \n' \
               '"balanced": prints whether the mobile is balanced or not \n' \
               '"print": prints the nodes in the mobile in preorder fashion \n' \
               '"infix": prints the nodes in the mobile in infix fashion \n' \
               '"find": finds and prints the nodes in the mobile \n' \
               '"weight" : prints the weights of the nodes in the mobile \n' \
               '"height" : prints the heights of the nodes in the mobile \n' \
               '"width" : print the width of the nodes in the mobile \n' \
               '"draw": draws the mobile'

    def quit(self):
        """
        Terminates the program when the user enters quit in the terminal
        :return: None
        """
        sys.exit(0)

    def balanced(self) -> int:
        """
        Checks if the mobile is balanced
        :return: returns the imbalance
        """
        return self.root.get_imbalance()

    def print(self):
        """
        Prints the preorder string representation of the node
        :return: None
        """
        print(self.root.print_pretty(''))

    def infix(self):
        """
        Get the infix string representation of the node
        :return: None
        """
        print(self.root.infix())

    def find_node(self, name):
        """
        Find a node by name
        :param name: the node's name
        :return: returns the name
        """
        return self.root.find(name)

    def weight_node(self, node):
        """
        Get the node's weight
        :param node: the node whose weight needs to be returned
        :return: the weight
        """
        return node.get_weight()

    def height_node(self, node):
        """
        Get the node's height
        :param node: the node whose height needs to be returned
        :return: the height
        """
        return node.get_height()

    def width_node(self, node):
        """
        Get the total node's width
        :param node: the node whose width needs to be returned
        :return: the total width
        """
        return node.get_width()

    def parse(self):
        """
        Parsing the file
        :return:
        """
        try:
            with open(self.filename) as file:
                for line in file:
                    self.node_data.append(line.strip())
                    if line.strip() == "":
                        break
        except FileNotFoundError as fe:
            print(fe)

    def create_node(self):
        """
        Creates the node
        :return:
        """
        node_split = self.node_data[self.index].split(" ")
        # checking if the first word is BALL and incrementing the index else
        if node_split[0] == "BALL":
            self.index += 1
            return Ball(node_split[1], int(node_split[2]), int(node_split[3]), int(node_split[4]))
        else:
            newNode = Rod(node_split[1], int(node_split[2]), int(node_split[3]), None, int(node_split[4]), None)
            self.index += 1
            newNode.left_child = self.create_node()
            newNode.right_child = self.create_node()
            return newNode

    def run(self):
        """
        The chunk where the commands and its methods are called which performs the required operations
        when the user enters a command
        :return: None
        """
        self.parse()
        self.root = self.create_node()
        while True:
            input_command = input().split(" ")
            # input_command = ['draw']
            # matching if the zero index consists of the input command
            match input_command[0]:
                # switch case for selection of commands and its respective function calls
                case 'root':
                    # printing the root
                    print(self.root)
                case 'help':
                    # printing the list of available help commands
                    print('> ' + 'help')
                    print(self.help())
                case 'quit':
                    # exits from the program
                    self.quit()
                case 'balanced':
                    # checks if root is balanced
                    print('> ' + 'balanced')
                    print(f'{self.root.get_name()}  balanced?  {self.root.is_balanced()}')
                    print(f'Imbalance amount:  {self.root.get_imbalance()}')
                case 'print':
                    # prints the whole mobile
                    print('> ' + 'print')
                    self.print()
                case 'weight':
                    # determining the weight
                    print(f'> weight {self.root.get_name()}')
                    node = self.find_node(input_command[1])
                    print(self.weight_node(node))
                case 'width':
                    # if the user enters width then the below lines get executed
                    print(f'> width {self.root.get_name()}')
                    node = self.find_node(input_command[1])
                    print(f'{self.root.get_name()} width? {self.width_node(node)}')
                case 'infix':
                    # if the user enters infix then the below lines get executed
                    print('> ' + 'infix')
                    self.infix()
                case 'find':
                    # if the user enters find then the below lines get executed
                    print(f'> find {self.root.get_name()}')
                    print(self.find_node(input_command[1]))
                case 'height':
                    # if the user enters height then the below lines get executed
                    print(f'> height {self.root.get_name()}')
                    node = self.find_node(input_command[1])
                    print(f'{self.root.get_name()} height? {self.height_node(node)}')
                case 'draw':
                    # used to draw the mobile coding by making a call to the turtle_init and the draw function
                    t = self.turtle_init()
                    t.right(90)
                    t.down()
                    self.root.draw(t)
                    t.mainloop()
                case _:
                    # if user enters any command which is not present in the list then the below message is printed
                    print("Incorrect command")


def main():
    """
    The main method of the program
    :return: returns nothing
    """
    print('Welcome to Mobiles App!')
    line = sys.argv[1].split('\\')[-1]
    print(f'{line} loaded and parsed!')
    print('Please enter "help" to know a list of commands available and then proceed further')
    if len(sys.argv) < 2:
        print("Usage: python mobile <mobile-file>")
        exit()
    filename = sys.argv[1]
    mobile = Mobile(filename)
    mobile.run()


if __name__ == '__main__':
    """
        The main program
        :return: nothing
        """
    main()
