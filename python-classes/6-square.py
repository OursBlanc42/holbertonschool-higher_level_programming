#!/usr/bin/python3

class Square:
    
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
        
    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return(self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for index in range(0, self.__size):
                for space in range (0, self.__position[0]):
                    print(" ",end = "")
                for index in range(0, self.__size):
                    print("#", end="")
                print("")
                    
    @property
    def position(self):
        return(self.__position)
    
    @position.setter
    def position(self, value):
        
        raise_error = False
        
        if not isinstance(value, tuple):
            raise_error = True
        
        if len(value) != 2:
            raise_error = True
            
        for number in value:
            if not isinstance(number, int):
                raise_error = True
            if number < 0:
                raise_error = True
        
        if raise_error == True:
            raise TypeError("position must be a tuple of 2 positive integers")
            
