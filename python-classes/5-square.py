#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size**2)

    def my_print(self):
        if self.__size is 0:
            print()

    for row in range(self.__size):
        for col in range(self.__size):
            print('{}'.format('#'), end="")
        print()
