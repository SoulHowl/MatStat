from info import *
from lab1 import generate_samps

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

init_n = 100
init_m = 10


def generate_data_for_f_via_intervals(samps, m):
    n = len(samps)
    xdots = [min(samps)] + [min(samps) + (max(samps) - min(samps)) * (i + 1) / m for i in range(m)]
    ydots = [0]
    ind = 0
    for i in range(m):
        cnt = 0
        while ind < n and samps[ind] <= xdots[i + 1]:
            ind += 1
            cnt += 1
        try:
            ydots += [cnt / n * m / (max(samps) - min(samps))]
        except ZeroDivisionError:
            ydots += [np.inf]
    xdots += [max(samps)]
    ydots += [0]
    return xdots, ydots


def generate_data_for_f_via_probabilities(samps, m):
    n = len(samps)
    if m > n: m = n
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


if __name__ == "__main__":

    init_data = generate_samps(init_n)
    init_data_intervals = generate_data_for_f_via_intervals(init_data, init_m)
    init_data_probabilities = generate_data_for_f_via_probabilities(init_data, init_m)

    print()
    print(f"n = {init_n}, m = {init_m}")
    print("intervals method")
    print("   y   |  f(y)")
    xdots, ydots = init_data_intervals
    for i in range(2, len(xdots) - 2):
        print("{:+.3f} | {:.3f}".format(xdots[i], ydots[i]))

    print()
    print("probabilities method")
    print("   y   |  f(y)")
    xdots, ydots = init_data_probabilities
    for i in range(2, len(xdots) - 2):
        print("{:+.3f} | {:.3f}".format(xdots[i], ydots[i]))

    fig, ax = plt.subplots()

    xplot = np.linspace(L - 1, R + 1, plotdots)
    yplot = [f(x) for x in xplot]

    realline, = plt.plot(xplot, yplot, linewidth=3, color='grey')
    intervalline, = plt.step(*init_data_intervals, where='pre', linewidth=3, color='blue')
    probabilityline, = plt.step(*init_data_probabilities, where='pre', linewidth=3, color='red')

    plt.subplots_adjust(left=0.1, bottom=0.25)

    n_slider = Slider(
        ax=plt.axes([0.15, 0.1, 0.5, 0.03]),
        label='n = 2 ^ ',
        valmin=0,
        valmax=15,
        valinit=0,
    )

    m_slider = Slider(
        ax=plt.axes([0.15, 0.05, 0.5, 0.03]),
        label='m = 2 ^ ',
        valmin=0,
        valmax=15,
        valinit=1,
    )


    def update(val):
        n = int(2 ** n_slider.val)
        m = int(2 ** m_slider.val)
        data = generate_samps(n)
        intervalline.set_data(*generate_data_for_f_via_intervals(data, m))
        probabilityline.set_data(*generate_data_for_f_via_probabilities(data, m))
        fig.canvas.draw_idle()


    n_slider.on_changed(update)
    m_slider.on_changed(update)

    button = Button(plt.axes([0.75, 0.1, 0.15, 0.05]), 'Generate')


    def generate(event):
        update(None)


    button.on_clicked(generate)

    plt.show()