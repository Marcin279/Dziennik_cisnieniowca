#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1. Dodanie nowej wartosci
2. Wyszukiwanie pomiarów po dacie
3. Wyszukiwanie pomiarow po wartosci
4. Wykres pomiarów
5. Średnia ciśnienia w danym miesiącu
"""
from add_new_position import *
from load_save_data import *
from average_in_month import *

def interface():
    string = f'1. Dodaj nowa wartość\n' \
             f'2. Wyszukiwanie po wartości\n' \
             f'3. Wyszukiwanie po dacie\n' \
             f'4. Zapis pomiarów do pliku\n' \
             f'5. Wykres wszystkich pomiarów\n' \
             f'6. Średnia ciśnienia w wybranym miesiącu\n' \
             f'0. Koniec\n'

    print(string)

data_base=[]


print("\nWitaj w Dzienniku Ciśnieniowca, oto dostępne funkcjonalnośći:\n")
load_data_base(data_base)
while True:
    interface()
    choice = input("Wybierz opcję z której chcesz skorzystać: ")
    if choice == '1':
        print("Not implemented")

    elif choice == '2':
        print("Not implemented")

    elif choice == '3':
        print("Not implemented")

    elif choice == '4':
        print("Not implemented")
        interface()

    elif choice == "5":
        print("Not implemented")

    elif choice == "6":
        month=input("Wybierz miesiąc:")
        year=input("Wybierz rok:")
        average_in_month(data_base,month,year)
    elif choice == '0':
        save_data_base(data_base)
        print("Koniec")
        break
    else:
        print("Nie ma takiej mozliwosci, Sprobuj ponownie")
        continue
