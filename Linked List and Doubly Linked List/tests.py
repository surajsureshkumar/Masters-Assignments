""" 
file: tests.py
description: Verify the LinkedHashSet class implementation
"""

__author__ = "YOUR NAME HERE"

from linked_hash_set import LinkedHashSet


def print_set(a_set):
    for word in a_set:  # uses the iter method
        print(word, end=" ")
    print()


def test0():
    table = LinkedHashSet(100)
    table.add("to")
    table.add("do")
    table.add("is")
    table.add("to")
    table.add("be")

    print_set(table)

    print("'to' in table?", table.contains("to"))
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_set(table)


def test1():
    """
    Adding elements into the table
    :return:
    """
    table = LinkedHashSet(100)
    table.add("")
    table.add("")
    table.add("")
    table.add("")
    table.add("")

    print_set(table)

    print("'to' in table?", table.contains("to"))
    table.remove("to")
    print("'to' in table?", table.contains("to"))
    table.add("")
    table.add("")
    table.add("")
    table.add("")
    table.add("")
    table.add("")
    table.add("")
    table.remove("")
    table.add("")
    table.add("")
    print_set(repr(table))
    table.add("")
    print(repr(table))

    print_set(table)


def test2():
    """
    Adding elements and removing all elements from the table
    :return:
    """
    table = LinkedHashSet(100)
    table.add("to")
    table.add("do")
    table.add("is")
    table.add("to")
    table.add("be")

    print_set(table)

    print("'to' in table?", table.contains("to"))
    table.remove("to")
    print("'to' in table?", table.contains("to"))
    table.add("a")
    table.add("b")
    table.add("c")
    table.add("d")
    table.add("e")
    table.add("f")
    table.add("g")
    table.remove("a")
    table.add("h")
    table.add("i")
    print_set(repr(table))
    table.add("j")

    table.remove("a")
    table.remove("b")
    table.remove("c")
    table.remove("d")
    table.remove("e")
    table.remove("f")
    table.remove("g")
    table.remove("h")
    table.remove("i")
    table.remove("be")
    table.remove("is")
    table.remove("j")
    table.remove("do")
    print(repr(table))

    print_set(table)


def test3():
    """
    Adding removing and checking if elements are present in table
    :return:
    """
    table = LinkedHashSet(100)
    table.add(1)
    table.add("dodo")
    table.add("isssss")
    table.add("tosss")
    table.add("beee")

    print_set(table)

    print("'to' in table?", table.contains("to"))
    table.remove("to")
    print("'to' in table?", table.contains("to"))
    table.add(None)
    table.add(None)
    table.add("sf")
    table.add("d")
    table.add("e")
    table.add("f")
    table.add("g")
    table.remove("a")
    table.add("h")
    table.add("i")
    print_set(repr(table))
    table.add("j")

    table.remove("a")
    table.remove("j")
    table.contains("j")
    table.contains("helloWorld")
    table.remove("do")
    table.add("isit")
    table.contains("amy")
    table.add("john")
    print(repr(table))

    print_set(table)


# create a test case to remove all items from the table and print it

if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
