

"""
Updated Wed 22 Feb
"""


def iterative_fib_seq(num):
    # iteration
    # 1 Parameter: depth
    # returns variable C: sum of twp previous numbers
    a = 0
    b = 1
    c = 0
    for i in range(num - 1):
        c = a + b
        a = b
        b = c
    return c


def rec_fib_seq(num):
    # recursion
    # 1 parameter: Depth

    # Recursive base
    if num <= 1:
        return num
    else:
        # Calls itself twice
        return rec_fib_seq(num - 1) + rec_fib_seq(num - 2)


def select_sort(arr):
    # cycle through the list
    for i in range(len(arr)):
        # def a minimum value
        min_value = i

        # cycle through i + 1 through len(value)
        for j in range(i + 1, len(arr)):
            # the if statement inside the for loop will then check whether the element value[i] is bigger then the next
            # element, value[i + 1]
            if arr[min_value] > arr[j]:
                # if the el[i] > el[i+ 1], convert the min_value to j (i + 1) to later swap the two,
                # therefore el[j + 1] < el[i]
                min_value = j
        # simple switching of values, so that the two elements will be swapped
        temp = arr[i]
        arr[i] = arr[min_value]
        arr[min_value] = temp
    return arr


def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        count = 0
        # a for loop that will cycle thorough the list
        for i in range(count, len(arr) - 1):
            # if el[1] is more than el[2] (4 > 3)
            if arr[count] > arr[count + 1]:
                # define a temporary variable that will hold el[1]
                temp = arr[count]
                # change el[1] to el[2] so the smaller number comes first in the list
                arr[count] = arr[count + 1]
                # switch el[2] to temp, which was el[1]. list = [el[2], el[1]] where el[2] < el[1]
                arr[count + 1] = temp
                # the two consecutive elements have been swapped
                flag = True
            # increase the count variable by one to check future el by el[n + 1]
            count += 1


def binary_search(arr, value):
    # 2 Parameters: array and value to find
    # Iterative
    # Returns position of element or -1 if element does noto exist
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1
