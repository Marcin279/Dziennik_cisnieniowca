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


def search_by_date():
    temp_list = []
    searching_date = input("Podaj date: ")
    date, blood_pressure_list = data_unpack()
    systolic_pressure = blood_pressure_list[0]
    diastolic_pressure = blood_pressure_list[1]
    blood_pressure = blood_pressure_list[2]

    n = len(date)

    for i in range(n):
        if searching_date == date[i]:
            temp_list.append(systolic_pressure[i])
            temp_list.append(diastolic_pressure[i])
            temp_list.append(blood_pressure[i])
    return temp_list if temp_list != [] else "Nie ma takiej daty"


def search_by_blood_pressure():
    temp_list = []
    searching_value = int(input("Podaj wartosc pulsu: "))
    date, blood_pressure_list = data_unpack()
    blood_pressure = blood_pressure_list[2]
    n = len(blood_pressure)

    for i in range(n):
        if searching_value == blood_pressure[i]:
            temp_list.append(date[i])

    return temp_list if temp_list != [] else "Nie ma takiej wartosci"

def search_by_systolic_pressure():
    temp_list = []
    searching_value = int(input("Podaj wartosc cisnienia skurczowego: "))
    date, blood_pressure_list = data_unpack()
    systolic_pressure = blood_pressure_list[0]
    n = len(systolic_pressure)

    for i in range(n):
        if searching_value == systolic_pressure[i]:
            temp_list.append(date[i])

    return temp_list if temp_list != [] else "Nie ma takiej wartosci"

def search_by_diastolic_pressure():
    temp_list = []
    searching_value = int(input("Podaj wartosc cisnienia rozkurczowego: "))
    date, blood_pressure_list = data_unpack()
    diastolic_pressure = blood_pressure_list[1]
    n = len(diastolic_pressure)

    for i in range(n):
        if searching_value == diastolic_pressure[i]:
            temp_list.append(date[i])

    return temp_list if temp_list != [] else "Nie ma takiej wartosci"
