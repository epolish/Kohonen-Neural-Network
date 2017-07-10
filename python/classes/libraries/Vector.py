from math import sqrt
from functools import reduce

class Vector:
    @staticmethod
    def module(vector):
        return sqrt(reduce((lambda x, y: x+y), map(lambda x: x**2, vector)))
    @staticmethod
    def multiplication(vector_a, vector_b):
        return reduce((lambda x, y: x+y), map(lambda x, y: x*y, vector_a, vector_b))
    @staticmethod
    def angle(vector_a, vector_b):
        return Vector.multiplication(vector_a, vector_b)/(Vector.module(vector_a) * Vector.module(vector_b))
    @staticmethod
    def normalize(vector):
        length = Vector.module(vector)
        return list(map(lambda x: x/length, vector))