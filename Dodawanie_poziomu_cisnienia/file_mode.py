#!/usr/bin/python
# -*- coding: utf-8 -*-
from add_new_position import input_data, add_data


# Działa, ale Przy otwieraniu pliku zaczyna od 2 lini - do poprawy
def write_data():
    filepath = "DC_baza_danych.txt"
    f = open(filepath, 'a', encoding="utf-8")
    x = input_data()
    date = x[0]
    systolic_pressure = x[1]
    diastolic_pressure = x[2]
    blood_pressure = x[3]

    data = add_data(date, systolic_pressure, diastolic_pressure, blood_pressure)
    string = ""
    for i in data:
        string += i
        string += "\t"

    string += "\n"

    f.write(string)
    f.close()


# Działa
def load_data():
    filepath = "DC_baza_danych.txt"
    f = open(filepath, 'r', encoding="utf-8")
    lst = f.read()

    lst = lst.splitlines(keepends=False)  # usuwa '\n'
    data_base = []
    for line in lst:
        if line != '':
            data_base.append((line.split()))
            f.close()
        else:
            f.close()

    return data_base  # Zwraca liste list


# Działa
def data_unpack():
    date = []  # Tworze osobne kontenery na date i wartosc cisnienia
    systolic_pressure = []
    diastolic_pressure = []
    blood_pressure = []

    x = load_data()  # Wczytywanie wartosci
    for i in x:
        date.append(i[0])
        systolic_pressure.append(int(i[1]))
        diastolic_pressure.append(int(i[2]))
        blood_pressure.append(int(i[3]))

    value = [systolic_pressure, diastolic_pressure, blood_pressure]
    return date, value  # Zwraca krotke tablic (data: str, wartosc: [int, int, int])

