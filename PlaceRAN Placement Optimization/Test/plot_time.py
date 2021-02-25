import math
import os
import matplotlib.pyplot as plt
import numpy as np


def error_measure(times):
    avg = sum(times) / len(times)
    soma = 0.0
    for i in times:
        soma = soma + (i - avg) ** 2
    var = soma / len(times)
    error = math.sqrt(var)
    return error


def plot_with_error(y, x, errors):
    yerror = errors

    plt.errorbar(x, y, yerr=yerror, fmt = ' ', ecolor='black', capsize=5)
    # assign your bars to a variable so their attributes can be accessed
    bars = plt.bar(x, height=y, width=.4)

    # access the bar attributes to place the text in the appropriate location
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .20, yval)
    plt.title("Random Capacity - Total")
    plt.xlabel("RU's Scenarios")
    plt.ylabel("Time (minutes)")
    plt.savefig("rdn_cap_total.png")
    plt.show()


if __name__ == '__main__':
    k = input("Fase? (1, 2, 3, 4 = total)")
    timesRU1 = []

    timesRU_0_1 = []

    for i in range(1, 6):
        file =  open("rnd_cap/ru1/teste{}.txt".format(i))
        time1 = file.readline().split(':')
        time2 = file.readline().split(':')
        time3 = file.readline().split(':')
        if k != 4:
            if k == 1:
                time = time1
            elif k == 2:
                time = time2
            elif k == 3:
                time = time3

            time = time[1].split(' ')
            time = time[1].split('\n')
            time = float(time[0]) / 60

        else:
            time1 = time1[1].split(' ')
            time1 = time1[1].split('\n')
            time1 = float(time1[0]) / 60

            time2 = time2[1].split(' ')
            time2 = time2[1].split('\n')
            time2 = float(time2[0]) / 60

            time3 = time3[1].split(' ')
            time3 = time3[1].split('\n')
            time3 = float(time3[0]) / 60

            time = time1 + time2 + time3

        print(time)
        timesRU1.append(time)

    for i in range(1, 6):
        file = open("rnd_cap/ru_0_1/teste{}.txt".format(i))
        time1 = file.readline().split(':')
        time2 = file.readline().split(':')
        time3 = file.readline().split(':')
        if k != 4:
            if k == 1:
                time = time1
            elif k == 2:
                time = time2
            elif k == 3:
                time = time3

            time = time[1].split(' ')
            time = time[1].split('\n')
            time = float(time[0]) / 60

        else:
            time1 = time1[1].split(' ')
            time1 = time1[1].split('\n')
            time1 = float(time1[0]) / 60

            time2 = time2[1].split(' ')
            time2 = time2[1].split('\n')
            time2 = float(time2[0]) / 60

            time3 = time3[1].split(' ')
            time3 = time3[1].split('\n')
            time3 = float(time3[0]) / 60

            time = time1 + time2 + time3

        timesRU_0_1.append(time)

    files = ["RU_1", "RU_0_1", "RU_0_3", "RU_1_3", "RU_3"]

    errorRU1 = error_measure(timesRU1)
    errorRU_0_1 = error_measure(timesRU_0_1)

    errors = []

    errors.append(errorRU1)
    errors.append(errorRU_0_1)
    errors.append(0)
    errors.append(0)
    errors.append(0)

    y = []
    y.append(float("{:.2f}".format(sum(timesRU1) / len(timesRU1))))
    y.append(float("{:.2f}".format(sum(timesRU_0_1) / len(timesRU_0_1))))
    y.append(0)
    y.append(0)
    y.append(0)
    print(y)

    plot_with_error(y, files, errors)

