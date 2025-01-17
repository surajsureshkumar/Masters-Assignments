# Implementation of stack and queue

from typing import Any, Optional


class LinkedNode:
    __slots__ = "value", "link"
    value: Any
    link: 'LinkedNode'

    def __init__(self, value: Any, link: 'LinkedNode' = None) -> None:
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.value)

    def __repr__(self) -> str:
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr(self.value) + "," + \
               repr(self.link) + ")"


class Stack:
    __slots__ = "top", "length"
    top: Optional[LinkedNode]
    length: int

    def __init__(self) -> None:
        """ Create a new empty stack."""
        self.top = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this stack, top value first.
        """
        result = "Stack["
        n = self.top
        while n is not None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, value: Any) -> None:
        self.top = LinkedNode(value, self.top)
        self.length += 1

    def pop(self) -> Any:
        assert not self.is_empty(), "Pop from empty stack"
        item = self.top.value
        self.top = self.top.link
        self.length -= 1
        return item

    def peek(self) -> Any:
        assert not self.is_empty(), "peek on empty stack"
        return self.top.value

    insert = push
    remove = pop


class Queue:
    __slots__ = "front", "back", "length"
    front: Optional[LinkedNode]
    back: Optional[LinkedNode]
    length: int

    def __init__(self) -> None:
        """ Create a new empty queue.
        """
        self.front = None
        self.back = None
        self.length = 0

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this queue, oldest value first.
        """
        result = "Queue["
        n = self.front
        while n is not None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def __len__(self):
        return self.length

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, value: Any) -> None:
        newNode = LinkedNode(value)
        if self.front is None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode
        self.length += 1

    def dequeue(self) -> Any:
        assert not self.is_empty(), "Dequeue from empty queue"
        item = self.front.value
        self.front = self.front.link
        if self.front is None:
            self.back = None
        self.length -= 1
        return item

    def peek(self) -> Any:
        assert not self.is_empty(), "peek on empty queue"
        return self.front.value

    insert = enqueue
    remove = dequeue
