from chain_node import ChainNode


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def __contains__(self, item):
        current = self.head
        while current:
            if current.obj == item:
                return True
            current = current.fwd
        return False

    def __str__(self):
        string = ""
        if self.head:
            start = self.head
            while start:
                string += str(start.obj)
                string += " -> "
                start = start.fwd
        return string + "None"

    def __repr__(self):
        string = ""
        if self.head:
            start = self.head
            while start:
                string += "{}".format(start.obj)
                if start.fwd:
                    string += ", "
                start = start.fwd
        return string

    def __bool__(self):
        return len(self) != 0

    def append(self, node: ChainNode):
        self.__count += 1
        if self.head is None:
            self.head = node
        else:
            start = self.head
            while start.fwd:
                start = start.fwd
            start.fwd = node

    def display(self):
        if self.head:
            start = self.head
            while start:
                print(start.obj, end=", ")
                start = start.fwd
            print()

    def delete(self, node):
        current = self.head
        if current:
            if current is node:
                self.head = current.fwd
                self.__count -= 1
                return

            while current.fwd and current.fwd is not node:
                current = current.fwd

            if current.fwd:
                current.fwd = node.fwd
                node.fwd = None
                self.__count -= 1

    def search(self, data):
        current = self.head
        while current:
            if current.obj == data:
                return current
            current = current.fwd
        return None