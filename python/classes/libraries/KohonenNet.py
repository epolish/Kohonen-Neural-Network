from copy import deepcopy
from classes.libraries.Matrix import *
from classes.libraries.Vector import *
from classes.libraries.Euclid import *

class KohonenNet(Vector, Matrix, Euclid):
    @property
    def method(self):
        return self.__method
        
    @property
    def iteration(self):
        return self.__iteration
        
    @method.setter
    def method(self, value):
        self.__method = value
        
    @iteration.setter
    def iteration(self, value):
        self.__iteration = value
        
    @staticmethod
    def era(P, W, k):
        self = KohonenNet
        return getattr(self, self.method)(P, W, k)
        
    @staticmethod
    def solve(P, W, k):
        self = KohonenNet
        self.iteration = 0
        Wprev = deepcopy(W)
        self.era(P, W, k)
        while Wprev != W:
            Wprev = deepcopy(W)
            self.era(P, W, k)
            self.iteration += 1
            if self.iteration == 99:
                break

    @staticmethod
    def byDist(P, W, k):
        self = KohonenNet
        lengthRow = len(P[0])
        lengthColumn = len(self.column(W, 0))
        for j in range(lengthRow):
            temp, index = 0, 0
            minimum = self.distance([a_i-b_i for a_i, b_i in zip(self.column(P, j), self.column(W, index))])
            for i in range(lengthColumn):
                temp = self.distance([a_i-b_i for a_i, b_i in zip(self.column(P, j), self.column(W, i))])
                if temp < minimum:
                    minimum = temp
                    index = i
            for i in range(lengthColumn):
                W[index][i] = W[index][i]+k*(P[i][j]-W[index][i])

    @staticmethod
    def byAngle(P, W, k):
        self = KohonenNet
        lengthRow = len(P[0])
        lengthColumn = len(self.column(W, 0))
        for j in range(lengthRow):
            i, temp, index, divider = 0, 0, 0, 0
            maximum = self.angle(self.column(P, j), self.column(W, i))
            for i in range(lengthColumn):
                temp = self.angle(self.column(P, j), self.column(W, i))
                if temp > maximum:
                    maximum = temp
                    index = i
            temp = self.module(self.column(W, index))
            for i in range(lengthColumn):
                divider += (self.column(W, index)[i]/temp+k*self.normalize(self.column(P, j))[i])**2
            divider = sqrt(divider)
            for i in range(lengthColumn):
                W[i][index] = (W[i][index]/temp+k*self.normalize(self.column(P, j))[i])/divider