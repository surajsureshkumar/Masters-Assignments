from typing import Optional

from chain_node import ChainNode


class DoublyLinkedListIterator:
    def __init__(self, head):
        """
        Constructor
        :param head:
        """
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        """
        Getting the next item in the list
        :return: item
        """
        if not self.current:
            raise StopIteration
        else:
            item = self.current.obj
            self.current = self.current.next
            return item


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def __iter__(self):
        """
        The iterator method
        :return: the head of the list
        """
        return DoublyLinkedListIterator(self.head)

    def __str__(self):
        string = ""
        if self.head:
            start = self.head
            while start:
                string += str(start.obj)
                if start.next:
                    string += ", "
                start = start.next
        return string

    def __contains__(self, item):
        current = self.head
        while current:
            if current.obj == item:
                return True
            current = current.next
        return False

    def __repr__(self):
        string = ""
        if self.head:
            start = self.head
            while start:
                string += "{}".format(start.obj)
                if start.next:
                    string += ", "
                start = start.next
        return string

    def __bool__(self):
        return len(self) != 0

    def append(self, node: ChainNode):
        # created a node so increment length
        self.__length += 1

        # if list is empty
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # if the list is not empty
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def delete(self, data) -> Optional[ChainNode]:
        """
        Delete the node containing the value = data
        :param data: data to be deleted
        :return: True upon deletion else False
        """
        current = self.head

        # if list is empty
        if current is None:
            return None

        # traverse till finding the node
        while current and current.obj != data:
            current = current.next

        # if current is false then we have not found the node to be deleted
        if not current:
            return None

        # now you have the node to be deleted, get the previous node reference
        prev_node = current.prev

        # if node to be deleted is head node
        if current == self.head:
            self.head = current.next

        # if node to be deleted is last node
        if current == self.tail:
            self.tail = current.prev

        # change next node's prev to prev_node of current node
        if current.next:
            current.next.prev = prev_node

        # change prev_node's next to current.next only if current is not head node
        if prev_node:
            prev_node.next = current.next

        # decrement the length property
        self.__length -= 1

        return current
