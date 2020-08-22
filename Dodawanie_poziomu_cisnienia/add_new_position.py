#!/usr/bin/python
# -*- coding: utf-8 -*-


def input_data():
    date_input = input("Podaj date:")
    blood_pressure_input = input("Podaj cisnienie krwi:")
    return [date_input, blood_pressure_input]


def add_data(date_input, blood_pressure_input):
    measurement_database = list()
    measurement_database.append(date_input)
    measurement_database.append(blood_pressure_input)
    return measurement_database
