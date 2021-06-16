from lab1.info import *
from lab1.lab1 import generate_samps, generate_data_for_F
from lab2.lab2 import generate_data_for_f_via_intervals, generate_data_for_f_via_probabilities

import numpy as np
import matplotlib.pyplot as plt

Kolmogorov = False

init_n = 2 ** 5


def data_error(samps, empiric):
    return max(abs(empiric[i] - F(samps[i])) for i in range(len(samps)))


def probability_density_ints(samps):
    m = int(len(samps) ** (1 / 3))
    xdots, ydots = generate_data_for_f_via_intervals(samps, m)
    if Kolmogorov:
        xdots = [x * init_n ** 0.5 for x in xdots]
        ydots = [y / init_n ** 0.5 for y in ydots]
    return xdots, ydots


def probability_density_probs(samps):
    m = int(len(samps) ** (1 / 3))
    xdots, ydots = generate_data_for_f_via_probabilities(samps, m)
    if Kolmogorov:
        xdots = [x * init_n ** 0.5 for x in xdots]
        ydots = [y / init_n ** 0.5 for y in ydots]
    return xdots, ydots


if __name__ == "__main__":

    worst_data = generate_data_for_F(init_n)
    worst_error = data_error(*worst_data)
    errors = [worst_error]
    try_cnt = 1

    import asyncio
    import aioconsole


    async def generate_worst_data():
        global worst_data
        global worst_error
        global try_cnt

        while True:
            try_cnt += 1
            test_data = generate_data_for_F(init_n)
            test_error = data_error(*test_data)
            errors.append(test_error)
            if test_error > worst_error:
                worst_data = test_data
                worst_error = test_error
            await asyncio.sleep(0)


    async def generate_until_stop():
        task = asyncio.create_task(generate_worst_data())
        await aioconsole.ainput('Press enter to stop generating')
        task.cancel()


    asyncio.run(generate_until_stop())

    errors.sort()

    print(f"n = {init_n}")
    print(f"Wostest data with {try_cnt} data_generations: abs(delta) = {worst_error}")
    if Kolmogorov: print(f"max K_x = {worst_error * init_n ** 0.5}")

    fig, ax = plt.subplots()

    xplot = np.linspace(L - 1, R + 1, plotdots)
    yplot = [F(x) for x in xplot]

    realline, = plt.plot(xplot, yplot, linewidth=3, color='grey')
    smoothline, = plt.plot(*worst_data, linewidth=3, color='orange')
    stepline, = plt.step(*worst_data, where='post', linewidth=2, color='blue')

    plt.show()

    fig, ax = plt.subplots()

    intervalline, = plt.step(*probability_density_ints(errors), where='pre', linewidth=3, color='blue', marker='o')
    probabilityline, = plt.step(*probability_density_probs(errors), where='pre', linewidth=3, color='red', marker='o')
    worst_error = max(errors)
    if Kolmogorov: worst_error *= init_n ** 0.5
    plt.plot([0], [0], 'o', markersize=0)
    plt.plot([worst_error], [1 / len(errors)], 'o', color='black', markersize=10)

    plt.show()