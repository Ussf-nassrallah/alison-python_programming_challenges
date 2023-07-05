"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            if width is less than 0, raise a ValueError exception with the message width must be >= 0
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            if height is less than 0, raise a ValueError exception with the message height must be >= 0
    Instantiation with optional width and height: def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the rectangle perimeter:
        if width or height is equal to 0, perimeter is equal to 0
    print() and str() should print the rectangle with the character(s) stored in print_symbol:
        if width or height is equal to 0, return an empty string
    repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
    Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
    You are not allowed to import any module

"""


class Rectangle:
    """ represen a Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def height(self):
        # Private instance attribute
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            p = 0
        else:
            p = (2 * self.width) + (2 * self.height)
        return p

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        w = self.width
        h = self.height
        sy = str(self.print_symbol)
        s = ""

        for y in range(0, h):
            for x in range(0, w):
                s += sy
            if y != h - 1:
                s += '\n'
        return s

    def __repr__(self):
        s = "Rectangle({}, {})".format(str(self.width), str(self.height))
        return s

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")