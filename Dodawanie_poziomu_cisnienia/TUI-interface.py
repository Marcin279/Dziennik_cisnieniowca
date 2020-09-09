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


def interface():
    string = f'1. Dodaj nowa wartosc\n' \
             f'2. Wyszukiwanie po wartosci\n' \
             f'3. Wyszukiwanie po dacie\n' \
             f'4. Wykres wszystkich pomiarow\n' \
             f'5. Średnia ciśnienia z wszystkich wartosci\n' \
             f'0. Koniec'
    print("\n")
    print(string)


while True:
    interface()
    choice = input("Wybierz opcję z której chcesz skorzystac: ")
    if choice == '1':
        file_mode.write_data()

    elif choice == '2':
        print(file_mode.search_by_value())

    elif choice == '3':
        print(file_mode.search_by_date())

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
