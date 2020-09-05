#!/usr/bin/python
# -*- coding: utf-8 -*-


def input_data():
    date_input = input("Podaj date:")
    blood_pressure_input = input("Podaj cisnienie krwi:")
    systolic_pressure_input = input("Podaj cisnienie skurczowe")
    diastolic_pressure_input = input("Podaj cisnienie rozkurczowe")
    return [date_input, blood_pressure_input, systolic_pressure_input, diastolic_pressure_input]


def add_data(date_input, blood_pressure_input, systolic_pressure, diastolic_pressure):
    measurement_database = list()
    measurement_database.append(date_input)
    measurement_database.append(blood_pressure_input)
    measurement_database.append(systolic_pressure)
    measurement_database.append(diastolic_pressure)
    return measurement_database
