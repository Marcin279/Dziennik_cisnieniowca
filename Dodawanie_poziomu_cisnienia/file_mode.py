#!/usr/bin/python
# -*- coding: utf-8 -*-
from add_new_position import input_data, add_data


# Działa, ale Przy otwieraniu pliku zaczyna od 2 lini - do poprawy
def write_data():
    filepath = "DC_baza_danych.txt"
    f = open(filepath, 'a', encoding="utf-8")
    x = input_data()
    date = x[0]
    blood_pressure = x[1]

    data = add_data(date, blood_pressure)
    string = ""
    for i in data:
        string += str(i)
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
    value = []
    x = load_data()  # Wczytywanie wartosci
    for i in x:
        date.append(i[0])
        value.append(int(i[1]))
    return date, value  # Zwraca krotke tablic (data: str, wartosc: int)


def search_by_date():
    temp_list = []
    searching_date = input("Podaj date: ")
    date, blood_pressure = data_unpack()
    n = len(date)
    # print(blood_pressure)
    for i in range(n):
        if searching_date == date[i]:
            # print(blood_pressure[i])
            temp_list.append(blood_pressure[i])

    return temp_list if temp_list != [] else "Nie ma takiej daty"


def search_by_value():
    temp_list = []
    searching_value = int(input("Podaj wartosc cisnienia krwi: "))
    date, blood_pressure = data_unpack()
    n = len(blood_pressure)
    for i in range(n):
        if searching_value == blood_pressure[i]:
            temp_list.append(date[i])

    return temp_list if temp_list != [] else "Nie ma takiej wartosci"


# print(load_data())
# print(data_unpack())
# write_data()
# print(search_by_date())
# print(search_by_value())



