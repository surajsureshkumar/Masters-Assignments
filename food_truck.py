"""
This is a program that demonstrates quick sort and quick select algorithm for a given input file
"""
import time
import random
import sys


def file_input(path):
    """
    Reading the file input
    :param path: path is the file to be opened
    :return: returns a list
    """
    lst = []
    with open(path) as file:
        for line in file:
            line = line.strip().split()
            lst.append(int(line[-1]))
    return lst


def quick_sort(items):
    """
    Performs the quick sort operation on a given list of data
    :param items: the list used to perform quick sort
    :return: a recursive function call to quick sort
    """
    length_of_list = len(items)
    # checking if items in list or else returns a empty list
    if not items:
        return []
    else:
        # selecting a random pivot element and getting the index
        pivot = random.randint(0, length_of_list - 1)
        # retrieving the element with the help of index
        pivot_element = items[pivot]
        # creating empty list to store the items and checking if items equal to pivot, lesser or greater than pivot
        items_greater = []
        items_lower = []
        equal_list = []
        # looping through the items list and checking if item is greater than or lesser than or equal to pivot
        for item in items:
            # if item greater than pivot, item is appended to items_greater
            if item > pivot_element:
                items_greater.append(item)
            # if item equal than pivot, items is appended to equal_list
            elif item == pivot_element:
                equal_list.append(item)
            # else item is appended to items_lower
            else:
                items_lower.append(item)
        return quick_sort(items_lower) + equal_list + quick_sort(items_greater)


def quick_select(items, k):
    """
    Performs the quick select operation on a given list of data
    :param items: the list used to perform quick select
    :param k: the index used to find the kth smallest element
    :return: recursive call to quick select
    """

    length_of_list = len(items)
    if not items:
        return 0
    else:
        # selecting a random pivot element and getting the index
        qs_pivot = random.randint(0, length_of_list - 1)
        # retrieving the element with the help of index
        pivot_element = items[qs_pivot]
        lower_array = []
        greater_array = []
        equal_array = []
        # looping through the items list and checking if item is greater than or lesser than or equal to pivot
        for item in items:
            # if item lesser than pivot_element, item is appended to lower_array
            if item < pivot_element:
                lower_array.append(item)
            # elif item equal to pivot_element, item is appended to equal_array
            elif item == pivot_element:
                equal_array.append(item)
            # elif item greater than pivot_element, item is appended to greater_array
            elif item > pivot_element:
                greater_array.append(item)
        # assigning the len of lower array to m
        m = len(lower_array)
        # getting the length of the equal array which contains similar elements in it
        elements_equal_pivot = len(equal_array)
        # checking if k is in between m and m+elements_equal_pivot and if found pivot is returned
        if m <= k < m + elements_equal_pivot:
            return pivot_element
        # if m greater than k then quick select is performed on the lower_array
        elif m > k:
            return quick_select(lower_array, k)
        # quick select is performed on the greater_array
        else:
            return quick_select(greater_array, k - m - elements_equal_pivot)


def main():
    """
    The main program
    :return: nothing
    """
    try:
        # checking if length of argument less than 2 if found returns a message
        if len(sys.argv) < 2:
            print("Usage: python3 food_truck.py input-file")
        else:
            # reading the file
            items = file_input(sys.argv[1])
            # counting the time
            start = time.perf_counter()
            qs = quick_sort(items)
            # calculating the elapsed time
            duration = time.perf_counter() - start
            print("File: ", sys.argv[1])
            print("Number of buildings: ", len(items))
            print("Using QuickSort to find optimal location")
            median = len(items) // 2
            # finding the sum of distance
            total_distance = sum([abs(i - qs[median]) for i in items])
            print("Elapsed time: ", duration, "seconds")
            print("Sum of distances: ", total_distance)
            print("---------------------------")
            start = time.perf_counter()
            k = len(items) // 2
            qs2 = quick_select(items, k)
            duration = time.perf_counter() - start
            print("File: ", sys.argv[1])
            print("Number of buildings: ", len(items))
            print("Using QuickSelect to find optimal location")
            # finding the sum of distance
            total_distance = sum([abs(i - qs2) for i in items])
            print("Elapsed time: ", duration, "seconds")
            print("Sum of distances: ", total_distance)
    except FileNotFoundError as fnfe:
        print(fnfe)


if __name__ == "__main__":
    main()
