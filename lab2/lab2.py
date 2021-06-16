from info import *
from lab1.lab1 import generate_samps

import numpy as np
import matplotlib.pyplot as plt


init_n = 100
init_m = 10


def generate_intervals(samps, m):
    n = len(samps)
    xdots = [min(samps)] + [min(samps) + (max(samps) - min(samps)) * (i + 1) / m for i in range(m)]
    ydots = [0]
    num_dots = []
    ind = 0
    for i in range(m):
        cnt = 0
        while ind < n and samps[ind] <= xdots[i + 1]:
            ind += 1
            cnt += 1
        num_dots.append(cnt)
        try:
            ydots += [cnt / n * m / (max(samps) - min(samps))]
        except ZeroDivisionError:
            ydots += [np.inf]
    xdots += [max(samps)]
    ydots += [0]
    return xdots, ydots, num_dots


def generate_probabilities(samps, m):
    n = len(samps)
    if m > n:
        m = n
    xdots = [min(samps)]
    ydots = [0]
    cnt = n / m
    prev_ind = 0
    for i in range(m):
        ind = int(n * (i + 1) / m - 1 / 2)
        xdots += [samps[ind]]
        try:
            ydots += [cnt / n / (samps[ind] - samps[prev_ind])]
        except ZeroDivisionError:
            ydots += [np.inf]
        prev_ind = ind
    xdots += [max(samps)]
    ydots += [0]
    return xdots, ydots

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
    #build_intervals(init_n,init_m)
    build_probabilities(init_n,init_m)

