#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List


class AddNewPosition:

    def __init__(self, date: str, systolic_pressure: int, diastolic_pressure: int, blood_pressure: int):
        self.date = date
        self.systolic_pressure = systolic_pressure
        self.diastolic_pressure = diastolic_pressure
        self.blood_pressure = blood_pressure

    def add(self):
        return [self.date, self.systolic_pressure, self.diastolic_pressure, self.blood_pressure]




lista1 = AddNewPosition("12.02.2020", 145, 74, 76)
lista2 = AddNewPosition("12.02.2026", 135, 76, 56)

listaglowna = [lista1.add(), lista2.add()]

print(listaglowna)







