#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(2)
    print(r1)

    r1.update(3, 2)
    print(r1)

    r1.update(4, 2, 3)
    print(r1)

    r1.update(5, 2, 3, 4)
    print(r1)

    r1.update(6, 2, 3, 4, 5)
    print(r1)