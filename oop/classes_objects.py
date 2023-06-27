"""
Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t fill lines by spaces when position[1] > 0
You are not allowed to import any module
"""


class Square:
    """ represent a square """
    def __init__(self, size=0, position=(0, 0)):
        """ create a new square """
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """ __size: private instance attribute """
        self.__size = value

    def my_print(self):
        n = self.__size
        if n == 0:
            print()
        for y in range(0, self.__position[1]):
            print("")
        for index in range(0, n):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, n):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or not all(isinstance(n, int) for n in value)
                or not all(n >= 0 for n in value)
                or len(value) != 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value