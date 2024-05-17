#!/usr/bin/python3

"""A square"""

class Square():

    """Define a class Square"""
   
    def __init__(self, width=0, height=0):
        """ Initialize the class """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        """ Description of a square """
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

