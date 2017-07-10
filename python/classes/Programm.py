import os
import json
import random
from classes.Method import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from classes.libraries.KohonenNet import *
from PyQt5 import QtCore

class Programm:
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value

    def randList(self, lower, upper, count):
        return [random.uniform(lower, upper) for _ in range(count)]

    def loadFromFile(self):
        with open(self.file) as data_file:    
            data = json.load(data_file)
        return data

    def saveToFile(self, file, data):
        with open(file[0] + '.result.json', 'w') as outfile:
            json.dump(data, outfile, indent = 4)

    def run(self, ratio):
        data = self.processData(self.getData(), ratio)
        self.saveToFile(os.path.splitext(self.file), [
            Matrix.transpose(data['dist']['W']), 
            Matrix.transpose(data['angle']['W'])
        ])
        self.draw(data)

    def processData(self, data, ratio):
        Wsecond = deepcopy(data['W'])
        KohonenNet.method = Method.DIST.value
        KohonenNet.solve(data['P'], data['W'], ratio)
        distIteration = KohonenNet.iteration+1
        KohonenNet.method = Method.ANGLE.value
        KohonenNet.solve(data['P'], Wsecond, ratio)
        angleIteration = KohonenNet.iteration+1
        return {
            'P' : data['P'],
            'dist' : { 'iteration' : distIteration, 'W' : data['W'] },
            'angle' : { 'iteration' : angleIteration, 'W' : Wsecond }
        }

    def getData(self):
        data = self.loadFromFile()
        if 'P' in data:
            P = data['P']
            if 'min' in data and 'max' in data and 'count' in data:
                W = [
                    self.randList(data['min'], data['max'], data['count']),
                    self.randList(data['min'], data['max'], data['count']),
                    self.randList(data['min'], data['max'], data['count'])
                ]
            else:
                W = data['W']
        else:
            raise Exception()
        return {'P' : P, 'W' : W}

    def draw(self, data):
        P = data['P']
        W = data['dist']['W']
        Wsecond = data['angle']['W']
        class_name = __class__.__name__
        plt.rc('font', size = 8, family = 'Verdana')
        _translate = QtCore.QCoreApplication.translate
        ax = plt.figure().add_subplot(111, projection = '3d')
        plt.title(_translate(class_name, 'Итерация: (Евклидово расстояние) = ') + str(data['dist']['iteration']) +
            _translate(class_name, '; (Угловое расстояние) = ') + str(data['angle']['iteration'])
        )
        ax.scatter(W[0], W[1], W[2],
            c = 'r', marker = 'o',  label = _translate(class_name, 'Координаты центров кластеров (Евклидово расстояние)')
        )
        ax.scatter(Wsecond[0], Wsecond[1], Wsecond[2],
            c = 'g', marker = 'o', label = _translate(class_name, 'Координаты центров кластеров (Угловое расстояние)')
        )
        ax.scatter(P[0], P[1], P[2],
            c = 'b', marker = '^',  label = _translate(class_name, 'Координаты точек')
        )
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        plt.legend(loc = 'upper left', numpoints = 1, ncol = 2, bbox_to_anchor = (0, 0))
        plt.show()