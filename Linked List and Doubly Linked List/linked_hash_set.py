from linkedlist import LinkedList
from doubly_linkedlist import DoublyLinkedList
from set import SetType
from chain_node import ChainNode


class LinkedHashSet(SetType):
    __slots__ = "initial_num_buckets", "capacity", "load_limit", "hash", "buckets", "order"

    MIN_BUCKETS = 10

    def __init__(self, initial_num_buckets: int = 100, load_limit: float = 0.75, hash_function=hash):
        """
        This is the constructor
        :param initial_num_buckets: the number of buckets
        :param load_limit: the maximum amount of load limit
        :param hash_function: assigning the inbuilt hash functions
        """
        super().__init__()
        self.initial_num_buckets = LinkedHashSet.MIN_BUCKETS if initial_num_buckets < 10 else initial_num_buckets
        self.capacity = self.initial_num_buckets
        self.load_limit = load_limit
        self.hash = hash_function
        self.buckets = self.create_buckets()
        self.order = DoublyLinkedList()

    def __iter__(self):
        """
        iter method invokes the DoublyLinkedList and access its methods to perform the iteration
        :return: the iter
        """
        return iter(self.order)

    def __len__(self) -> int:
        """
        The len of the table
        :return: the size
        """
        return self.size

    def __repr__(self) -> str:
        """
        Returns the object representation in string format
        :return: string
        """

        string = f"Capacity: {self.capacity}, Size: {self.size}, " \
                 f"Load Factor: {self.get_load_factor()}, Load Limit: {self.load_limit}\n"
        string += "\tHash table\n"
        string += "\t----------\n"
        for i in range(self.capacity):
            string += f"\t{i}: {self.buckets[i]}\n"
        return string

    def __str__(self) -> str:
        """
        This method returns the string representation of the object
        :return: string
        """
        string = "{"
        string += str(self.order)
        return string + "}"

    def re_initialize(self, capacity):
        hash_set = self.order
        self.capacity = capacity
        self.buckets = self.create_buckets()
        self.size = 0
        self.order = DoublyLinkedList()

        for item in hash_set:
            self.add(item)

    def create_buckets(self):
        """
        Creating the buckets
        :return: a linkedlist
        """
        return [LinkedList() for _ in range(self.capacity)]

    def validate_load_limit(self):
        """
        Validating the load limit
        :return: None
        """
        if self.is_limit_reached():
            self.re_initialize(self.capacity * 2)

        if self.size == 0 and self.capacity > 50:
            self.re_initialize(50)

    def add(self, obj):
        """
        Adding elements to the table
        :param obj: the object
        :return: Bool
        """
        self.validate_load_limit()

        if self.contains(obj):
            return

        node = ChainNode(obj)
        self.buckets[self.hashcode(obj)].append(node)
        self.order.append(node)
        self.size += 1

    def hashcode(self, obj) -> int:
        """
        Computing the hashcode
        :param obj: the object
        :return: int
        """
        return self.hash(obj) % self.capacity

    def contains(self, obj) -> bool:
        """
        Checks if the element is present in the table
        :param obj: the object in the table
        :return: bool
        """
        return obj in self.buckets[self.hashcode(obj)]

    def remove(self, obj):
        """
        Removing the element from the table
        :param obj:
        :return:
        """
        node = self.order.delete(obj)

        # obj not found in the doubly linked list
        if not node:
            return

        self.buckets[self.hashcode(obj)].delete(node)
        self.size -= 1
        self.validate_load_limit()

    def get_load_factor(self) -> float:
        """
        Computing the load factor
        :return: float value
        """
        return self.size and self.size / len(self.buckets)

    def is_limit_reached(self):
        """
        Checking if table limit is reached
        :return:
        """
        return self.get_load_factor() >= self.load_limit
