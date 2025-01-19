class ChainNode:
    __slots__ = "obj", "prev", "next", "fwd"

    def __init__(self, obj: any, prev: 'ChainNode' = None, next: 'ChainNode' = None, fwd: 'ChainNode' = None):
        """
        The constructor
        :param obj: the object
        :param prev: ordering link
        :param next: hash table link
        :param fwd:ordering link
        """
        self.obj = obj
        self.prev = prev
        self.next = next
        self.fwd = fwd

    def __repr__(self) -> str:
        """
        Returns the object representation in string format
        :return: string
        """
        return str(self.obj)

    def __str__(self) -> str:
        """
        This method returns the string representation of the object
        :return: string
        """
        return f'{self.obj}'
