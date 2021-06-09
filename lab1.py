from info import *

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

init_n = 27


def generate_samps(n):
    samps = [Y() for i in range(n)]
    samps.sort()
    return samps


def generate_data_for_F(n):
    samps = [L - 1, L] + generate_samps(n) + [R, R + 1]
    empiric = [0, 0] + [(i + 1) / n for i in range(n)] + [1, 1]
    return samps, empiric


if __name__ == "__main__":

    init_data = generate_data_for_F(init_n)

    print()
    print(f"n = {init_n}")
    print("   y   |  F(y)")
    xdots, ydots = init_data
    for i in range(2, len(xdots) - 2):
        print("{:+.3f} | {:.3f}".format(xdots[i], ydots[i]))

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)

    xplot = np.linspace(L - 1, R + 1, plotdots)
    yplot = [F(x) for x in xplot]

    realline, = plt.plot(xplot, yplot, linewidth=3, color='grey')
    smoothline, = plt.plot(*init_data, linewidth=3, color='orange')
    stepline, = plt.step(*init_data, where='post', linewidth=2, color='blue')

    n_slider = Slider(
        ax=plt.axes([0.15, 0.1, 0.5, 0.03]),
        label='n = 2 ^ ',
        valmin=0,
        valmax=15,
        valinit=0,
    )


    def update(val):
        n = int(2 ** n_slider.val)
        data = generate_data_for_F(n)
        smoothline.set_data(*data)
        stepline.set_data(*data)
        fig.canvas.draw_idle()


    n_slider.on_changed(update)

    button = Button(plt.axes([0.75, 0.1, 0.15, 0.05]), 'Generate')


    def generate(event):
        update(None)


    button.on_clicked(generate)

    plt.show()
    #plt.savefig("lab1.png")