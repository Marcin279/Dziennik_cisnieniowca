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
    sys = []
    blood = []
    dias = []
    dates = []
    for mon in get_month():
        if month == mon:
            dates.append(date[i])
            sys.append(systolic_pressure[i])
            dias.append(diastolic_pressure[i])
            blood.append(blood_pressure[i])
            # plt.plot(date[i], systolic_pressure[i], 'go', label=)
            # plt.plot(date[i], diastolic_pressure[i], 'ro')
            # plt.plot(date[i], blood_pressure[i], 'bo')
        i += 1

    plt.plot(dates, sys, 'o', label="Cisnienie skurczowe")
    plt.plot(dates, dias, 'ro', label="Cisnienie rozkurczowe")
    plt.plot(dates, blood, 'bo', label="Puls")
    plt.title("Wykres")
    plt.xlabel("Data")
    plt.ylabel("Wartosci cisnienia")
    plt.legend(loc='best', shadow=True, fontsize=12)
    plt.show()


