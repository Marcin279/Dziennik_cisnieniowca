#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from file_mode import data_unpack

x = data_unpack()

date = x[0]
values = x[1]


# Funkcja otrzymuje jako parametr miesiąc i rok i rysuje wykres z podanego okresu
def plot_diagram(dates):
    systolic_pressure = values[0]
    diastolic_pressure = values[1]
    blood_pressure = values[2]
    j = 0
    sys = []
    blood = []
    dias = []
    dates_list = []

    for i in date:
        if dates == i[3:]:
            dates_list.append(date[j])
            sys.append(systolic_pressure[j])
            dias.append(diastolic_pressure[j])
            blood.append(blood_pressure[j])
        j += 1

    plt.plot(dates_list, sys, 'o', label="Cisnienie skurczowe")
    plt.plot(dates_list, dias, 'ro', label="Cisnienie rozkurczowe")
    plt.plot(dates_list, blood, 'bo', label="Puls")
    plt.title("Wykres")
    plt.xlabel("Data")
    plt.ylabel("Wartosci cisnienia")
    plt.legend(loc='best', shadow=True, fontsize=12)
    plt.show()


