from math import sqrt
from functools import reduce

class Euclid:
    @staticmethod
    def distance(vector):
        return sqrt(reduce((lambda x, y: x+y), map(lambda x: x**2, vector)))