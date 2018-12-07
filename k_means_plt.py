#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import argparse
from k_means_calc import K_means
colorlist = ("r", "g", "b", "c", "m", "y", "k", "w")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k',
                        '--k_means',
                        help='いくつクラスタを作るか',
                        type=int,
                        default=2
                        )
    parser.add_argument('-d',
                        '--data',
                        help='いくつのデータで行うか',
                        type=int,
                        default=20)
    args = parser.parse_args()
    k = args.k_means
    data = args.data

    k_means = K_means(k, data)

    for x, y in zip(k_means.data_X, k_means.data_Y):
        plt.scatter(x, y, c='black')
    plt.show()

    for x, y in zip(k_means.data_X, k_means.data_Y):
        plt.scatter(x, y, c='black')
    for i, (x, y) in enumerate(zip(k_means.centroid_X, k_means.centroid_Y)):
        plt.scatter(x, y, c=colorlist[i],
                    marker='*',
                    label='center{}'.format(i+1))
    plt.legend()
    plt.show()

    while 1:
        for i, (x, y) in enumerate(
         zip(k_means.centroid_X, k_means.centroid_Y)):
            plt.scatter(x, y, c=colorlist[i],
                        marker='*',
                        label='center{}'.format(i+1))
        label = k_means.near_dis()
        for i, (x, y) in zip(label, zip(k_means.data_X, k_means.data_Y)):
            plt.scatter(x, y, c=colorlist[i])
        plt.legend()
        plt.show()
        X, Y = np.copy(k_means.centroid_X), np.copy(k_means.centroid_Y)
        k_means.fit()
        print(k_means)
        if (X == k_means.centroid_X).all() and (Y == k_means.centroid_Y).all():
            print('最終結果')
            print(k_means)
            break
