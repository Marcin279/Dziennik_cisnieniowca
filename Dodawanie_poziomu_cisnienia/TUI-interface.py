#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1. Dodanie nowej wartosci
2. Wyszukiwanie pomiarów po dacie
3. Wyszukiwanie pomiarow po wartosci
4. Wykres pomiarów
5. Średnia ciśnienia w danym miesiącu
"""
import file_mode
from searching_mode import search_by_date, search_by_blood_pressure, search_by_diastolic_pressure
from searching_mode import search_by_systolic_pressure

def interface():
    string = f'1. Dodaj nowa wartosc\n' \
             f'2. Wyszukiwanie po wartosci\n' \
             f'3. Wyszukiwanie po dacie\n' \
             f'4. Wykres wszystkich pomiarow\n' \
             f'5. Średnia ciśnienia z wszystkich wartosci\n' \
             f'0. Koniec'
    print("\n")
    print(string)


def interface2():
    string = f'1. Szukaj po wartosci pulsu\n' \
             f'2. Szukaj pow wartosci cisnienia skurczowego\n' \
             f'3. Szukaj pow wartosci cisnienia rozkurczowego\n' \
             f'0. Koniec'
    print("\n")
    print(string)


while True:
    interface()
    choice = input("Wybierz opcję z której chcesz skorzystac: ")
    if choice == '1':
        file_mode.write_data()

    elif choice == '2':
        while True:
            interface2()
            choice = input("Wybierz opcję z której chcesz skorzystac: ")

            if choice == '1':
                print(search_by_blood_pressure())
            elif choice == '2':
                print(search_by_systolic_pressure())
            elif choice == '3':
                print(search_by_diastolic_pressure())
            elif choice == '0':
                print("Koniec")
                break
            else:
                print("Nie ma takiej wartosci spróbuj ponownie")

    elif choice == '3':
        print(search_by_date())

    elif choice == '4':
        print("Not implemented")
        interface()

    elif choice == "5":
        print("Not implemented")

    elif choice == '0':
        print("Koniec")
        break
    else:
        print("Nie ma takiej mozliwosci, Sprobuj ponownie")
        continue
