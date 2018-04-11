#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

class IterateMe_2(IterateMe_1):
    def __init__(self, start = 0, stop = 5, step = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.start < self.stop:
            current_return = self.start
            self.start += self.step
            return current_return
        else:
            raise StopIteration
        
if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)

    print("Testing iterator 2")
    it = IterateMe_2(2,20,2)
    for i in it:
        if i > 10:
            break
        print(i)
        
    print("Testing iterator 2 after break")
    for i in it:
        print(i)
