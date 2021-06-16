from info import *
from lab1.lab1 import generate_samps

import numpy as np
import matplotlib.pyplot as plt


init_n = 100
init_m = 10


def generate_intervals(samps, m):
    n = len(samps)
    xnums = [min(samps)] + [min(samps) + (max(samps) - min(samps)) * (i + 1) / m for i in range(m)]
    ynums = [0]
    num_dots = []
    ind = 0
    for i in range(m):
        count = 0
        while ind < n and samps[ind] <= xnums[i + 1]:
            ind += 1
            count += 1
        num_dots.append(count)
        try:
            ynums += [count / n * m / (max(samps) - min(samps))]
        except ZeroDivisionError:
            ynums += [np.inf]
    xnums += [max(samps)]
    #ydots += [0]
    return xnums, ynums, num_dots


def generate_probabilities(samps, m):
    n = len(samps)
    if m > n:
        m = n
    xnums = [min(samps)]
    ynums = [0]
    cnt = n / m
    prev_ind = 0
    for i in range(m):
        ind = int(n * (i + 1) / m - 1 / 2)
        xnums += [samps[ind]]
        try:
            ynums += [cnt / n / (samps[ind] - samps[prev_ind])]
        except ZeroDivisionError:
            ynums += [np.inf]
        prev_ind = ind
    xnums += [max(samps)]
    #ydots += [0]
    return xnums, ynums

import matplotlib.patches as patches


def build_intervals(n, m):
    fig, ax1 = plt.subplots()
    init_data = generate_samps(init_n)
    init_data_intervals = generate_intervals(init_data, init_m)

    print()
    print(f"n = {init_n}, m = {init_m}")
    print("intervals method")
    print("   y   |  f(y)")
    xdots, ydots, nums = init_data_intervals
    for i in range(1, len(xdots) - 1):
        print("{:+.3f} | {:.3f}".format(xdots[i], ydots[i]))
    xplot = np.linspace(L - 1, R + 1, plotdots)
    yplot = [f(x) for x in xplot]
    plt.plot(xplot, yplot, linewidth=3, color='red')
    ax, ay, nums = init_data_intervals
    ax1.plot([-1, 4], [0,0])
    for j in range(m):
        ax1.add_patch(
            patches.Rectangle(
                (ax[j], 0),
                ax[j+1]-ax[j],
                ay[j+1],
                edgecolor='blue',
                facecolor='red',
                fill=False
            ))
    #print(nums)
    for i in range(m):
        nums[i] /= n
    xnums = []
    for i in range(m):
        xnums.append((ax[i] + ax[i+1]) / 2)
    #plt.scatter(xnums, nums)
    plt.plot(xnums, nums)
    plt.show()


def build_probabilities(n, m):
    fig, ax1 = plt.subplots()
    init_data = generate_samps(init_n)
    init_data_probabilities = generate_probabilities(init_data, init_m)

    print()
    print("probabilities method")
    print("   y   |  f(y)")
    xdots, ydots = init_data_probabilities
    for i in range(1, len(xdots) - 1):
        print("{:+.3f} | {:.3f}".format(xdots[i], ydots[i]))

    xplot = np.linspace(L - 1, R + 1, plotdots)
    yplot = [f(x) for x in xplot]
    plt.plot(xplot, yplot, linewidth=3, color='red')
    ax, ay = init_data_probabilities
    ax1.plot([-1, 4], [0,0])
    for j in range(m):
        ax1.add_patch(
            patches.Rectangle(
                (ax[j], 0),
                ax[j+1]-ax[j],
                ay[j+1],
                edgecolor='blue',
                facecolor='red',
                fill=False
            ))

    nums = [m/n] * m
    xnums = []
    for i in range(m):
        xnums.append((ax[i] + ax[i+1]) / 2)
    plt.plot(xnums, nums)

    plt.show()


if __name__ == "__main__":
    #init_n = int(input())
    #init_m = round(init_n ** 0.5)
    build_intervals(init_n,init_m)
    #build_probabilities(init_n,init_m)

