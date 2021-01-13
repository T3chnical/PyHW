# Louis

"""
Problem 1
Return the average of a list of values using a while loop.
"""


def while_average(arr):
    a = 0
    sum = 0
    while sum < len(arr):
        a += arr[sum]
        sum += 1
    return a / len(arr)


"""
Problem 2
Return the average of a list of values using a for loop.
"""


def loop_average(arr):
    num = 0
    for a in arr:
        num += 1
    return num / len(arr)


"""
Problem 3
Return the number of palindromes in a list. A palindrome is a word that is the same when spelled backwards. 
"""


def palindromes(arr):
    a = 0
    for b in arr:
        if b == b[::-1]:
            a += 1
    return a


"""
Problem 4
Return the maximum value of a list. Do not use the max() function.
"""


def list_max(arr):
    bigboi = 0
    for a in arr:
        if a > bigboi:
            bigboi = 1
    return bigboi


"""
Problem 5
Given a string representing a binary (base 2) number, return its decimal representation as an int. Decimal
numbers (base 10) are the numbers that we are used to, such as 0, 1, 2, 3,...
Binary works using powers of 2, where starting from the right, the first value represents 2 ** 0, 
the second is 2 ** 1, and so on. You multiply that power of 2 by the number in that position
in the string, either 1 or 0, and add it to a sum. 
Let's take 10011 as an example.
Starting from the right:
(2 ** 0) * 1 = 1
(2 ** 1) * 1 = 2
(2 ** 2) * 0 = 0
(2 ** 3) * 0 = 0
(2 ** 4) * 1 = 16
Those numbers add up to 19.
More information here: https://www.tutorialspoint.com/how-to-convert-binary-to-decimal
You should use the function int(), which can convert strings into ints. For example, int("1") returns 1 as an int.
"""


def binary(str):
    a = 0
    for num in str:
        a *= 2
        a += int(num)
        return a