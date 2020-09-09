#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import file_mode

x = file_mode.data_unpack()

date = x[0]
values = x[1]


def get_month():
    temp = []
    for i in date:
        temp.append(i.split('.'))

    month = []
    for j in temp:
        month.append(int(j[1]))

    return month  # list(int)


# # TODO: Do usunięcia, używane do testów
# selected_month = int(input("Podaj miesiac, z ktorego chcesz miec wyniki: "))


# Funkcja otrzymuje jako parametr miesiąc i rysuje wykres z podanego miesiąca
def plot_diagram(month: int):
    systolic_pressure = values[0]
    diastolic_pressure = values[1]
    blood_pressure = values[2]
    i = 0
    for mon in get_month():
        if month == mon:
            plt.plot(date[i], systolic_pressure[i], 'go')
            plt.plot(date[i], diastolic_pressure[i], 'ro')
            plt.plot(date[i], blood_pressure[i], 'bo')

        i += 1
    plt.title("Wykres")
    plt.xlabel("Data")
    plt.ylabel("Wartosci cisnienia")
    plt.show()


