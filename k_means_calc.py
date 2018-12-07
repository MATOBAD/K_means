#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math


class K_means:
    def __init__(self, k, d):
        '''
        k: クラスタの数
        d: データの数
        centroid: 重心
        '''
        self.k_num = k
        self.centroid_X = np.random.randint(0, 100, k)
        self.centroid_Y = np.random.randint(0, 100, k)
        self.data_X = np.random.randint(0, 100, d)
        self.data_Y = np.random.randint(0, 100, d)
        self.iter = 0

    def __distance(self, x1, x2, y1, y2):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return math.sqrt(dx**2+dy**2)

    def near_dis(self):
        self.label = []
        for x1, y1 in zip(self.data_X, self.data_Y):
            near_d = 1000
            near_i = 10
            for i, (x2, y2) in enumerate(zip(self.centroid_X, self.centroid_Y)):
                d = self.__distance(x1, x2, y1, y2)
                if near_d > d:
                    near_d = d
                    near_i = i
            self.label.append(near_i)
        return self.label

    def fit(self):
        self.iter += 1
        label = np.array(self.label)
        for k in range(self.k_num):
            s_x = sum(self.data_X[label == k])
            s_y = sum(self.data_Y[label == k])
            n = len(self.data_X[label == k])
            self.centroid_X[k] = s_x / n
            self.centroid_Y[k] = s_y / n

    def __str__(self):
        centeroid = []
        sent = '学習回数: {}\n'.format(self.iter)
        for i, (X, Y) in enumerate(zip(self.centroid_X, self.centroid_Y)):
            sent += 'center: {0}, X: {1}, Y: {2}\n'.format(i+1, X, Y)
        return sent
