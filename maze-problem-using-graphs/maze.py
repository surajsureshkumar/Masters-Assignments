"""
CSCI-603: Assignment 9
Author: Suraj Sureshkumar (ss7495@g.rit.edu)

This is a homework program that draws the ice maze graphs and displays the paths to escape from it
"""

# Import statements
import sys
from graph import Graph
from searchAlgos import findShortestPath


class IceMaze:
    __slots__ = 'graph', 'paths', 'data', 'rows', 'cols', 'filename', 'escape'

    def __init__(self, filename):
        """
        Constructor
        :param filename: the name of the file
        """
        self.graph = Graph()
        self.data = []
        self.rows = 0
        self.cols = 0
        self.filename = filename
        self.escape = 0

    def file_parser(self):
        """
        Parses the input file
        :return: None
        """
        with open(self.filename) as file:
            line = file.readline()
            line = line.split(" ")
            self.rows = int(line[0])
            self.cols = int(line[1])
            self.escape = int(line[2])
            for line in file:
                without_newline = line[:-1].split(" ")
                self.data.append(without_newline)
            self.graph_creation()

    def graph_creation(self):
        """
        Creating the graph
        :return: None
        """
        for r in range(0, self.rows):  # Looping through the rows
            for c in range(0, self.cols):  # Looping through the columns
                self.add_neighbors(r, c)
        self.show_paths()

    def show_paths(self):
        """
        Showing the possible paths in the ice maze
        :return: None
        """
        lst = []
        escape_dict = {}
        for r in range(0, self.rows):  # Looping through the rows
            for c in range(0, self.cols):  # Looping through the columns
                if self.data[r][c] == "*":  # checking if the current node is a rock and if it is a rock then continue
                    continue
                # if column and row not equal to colum-1 and escape we find the shortest path and store it in path
                if (c, r) != (self.cols - 1, self.escape):
                    path = findShortestPath(self.graph.getVertex((c, r)),
                                            self.graph.getVertex((self.cols - 1, self.escape)))
                    # If path is none then steps is 0 or else decrement path by 1
                    if path is None:
                        steps = 0
                    else:
                        steps = len(path) - 1
                else:
                    steps = 1
                # checking if steps not in escape_dict
                if steps not in escape_dict.keys():
                    escape_dict[steps] = [(c, r)]
                else:
                    escape_dict[steps].append((c, r))

        # Looping through each key in dict and checking if key is 0 then no path exists else the path gets printed
        for key in sorted(list(escape_dict.keys())):
            if key == 0:
                print('No path' + ": " + str(escape_dict[key]))
            else:
                print(str(key) + ": " + str(escape_dict[key]))

    def add_neighbors(self, r, c):
        """
        Adding the neighbors to the right left top and bottom
        :param r: rows
        :param c: column
        :return: None
        """
        # checking if the current path is stone,if it is not then we add the neighbors
        if self.data[r][c] != "*":
            self.add_neighbor((c, r), self.find_right_neighbor(r, c))
            self.add_neighbor((c, r), self.find_left_neighbor(r, c))
            self.add_neighbor((c, r), self.find_up_neighbor(r, c))
            self.add_neighbor((c, r), self.find_down_neighbor(r, c))

    def add_neighbor(self, src, dest):
        """
        Checking if the source and destination are the same, if not then add a new edge
        :param src: Source node
        :param dest: destination node
        :return: None
        """
        if src != dest:
            self.graph.addEdge(src, dest, 1)

    def find_right_neighbor(self, r, c):
        """
        finding the right neighbor and stopping right before the stone
        :param r: rows
        :param c: columns
        :return: stopper and row
        """
        stopper = self.cols - 1
        # Looping through the columns
        for i in range(c + 1, self.cols):
            # Checking if the node is a stone and if stone then decrement the stopper
            if self.data[r][i] == "*":
                stopper = i - 1
                break
        return stopper, r

    def find_left_neighbor(self, r, c):
        """
        finding the left neighbor and stopping right before the stone
        :param r: row
        :param c: column
        :return: stopper and row
        """
        stopper = 0
        # Looping through the columns by reducing the number of columns if we are at the center or similar position
        for i in range(c - 1, -1, -1):
            # Checking if the node is a stone and if stone then increment the stopper
            if self.data[r][i] == "*":
                stopper = i + 1
                break
        return stopper, r

    def find_up_neighbor(self, r, c):
        """
        finding the up neighbor and stopping right before the stone
        :param r: row
        :param c: column
        :return: column and stopper
        """
        stopper = 0
        # Looping through the rows by reducing the number of rows if we are at the bottom or similar position
        # which is not the top
        for i in range(r - 1, -1, -1):
            # Checking if the node is a stone and if stone then increment the stopper
            if self.data[i][c] == "*":
                stopper = i + 1
                break
        return c, stopper

    def find_down_neighbor(self, r, c):
        """
        finding the down neighbor and stopping right before the stone
        :param r: row
        :param c: column
        :return: column and stopper
        """
        stopper = self.rows - 1
        # Looping through the rows by reducing the number of rows if we are at the top or similar position
        for i in range(r + 1, self.rows):
            # Checking if the node is a stone and if stone then increment the stopper
            if self.data[i][c] == "*":
                stopper = i - 1
                break
        return c, stopper


def main():
    """
    Main method
    :return: None
    """
    # Taking input as argument
    filename = sys.argv[1]
    ice_maze = IceMaze(filename)
    ice_maze.file_parser()


if __name__ == '__main__':
    main()
