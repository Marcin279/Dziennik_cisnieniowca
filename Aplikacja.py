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
from searching_mode import *
from file_mode import *
from diagram import *


def interface():
    string = f'1. Dodaj nowa wartość\n' \
             f'2. Wyszukiwanie po dacie i wartości\n' \
             f'3. Wykres pomiarów\n' \
             f'4. Średnia ciśnienia w wybranym miesiącu\n' \
             f'0. Koniec\n'

    print(string)

data_base=[]
new_datas=[]

print("\nWitaj w Dzienniku Ciśnieniowca, oto dostępne funkcjonalnośći:\n")
load_data_base(data_base)
while True:
    interface()
    choice = input("Wybierz opcję z której chcesz skorzystać: ")
    if choice == '1':
        print("\nFormat daty - dzien.miesiac.rok")
        new = input_data()
        data_base.append(add_data(new[0],new[1],new[2],new[3]))
        new_datas.append(add_data(new[0],new[1],new[2],new[3]))
        print("\n")
    elif choice == '2':
        print(f'\n1.Wyszukiwanie po dacie \n' 
            f'2.Wyszukiwanie po ciśnieniu skurczowym\n' 
            f'3.Wyszukiwanie po ciśnieniu rozkurczowym\n' 
            f'4.Wyszukiwanie po pulsie\n')
        choice = input("Wybierz po czym chcesz wyszukać:")
        to_print_list = []
        data_base_search = load_data()
        if choice == '1':
            to_print_list = search_by_date()
        elif choice == '2':
            to_print_list = search_by_systolic_pressure()
        elif choice == '3':
            to_print_list = search_by_diastolic_pressure()
        elif choice == '4':
            to_print_list = search_by_blood_pressure()
        else:
            print("Spróbuj ponownie")
        print("\nZnalezione wartości:")
        print(to_print_list)
        print("\n")
    elif choice == '3':
        selected_month = (input("\nPodaj miesiac(np: 09.20), z ktorego chcesz miec wyniki: "))
        plot_diagram(selected_month)
        print("\n")
    elif choice == "4":
        month = input("Wybierz miesiąc:")
        year = input("Wybierz rok:")
        average_in_month(data_base, month, year)
    elif choice == '0':
        save_data_base(new_datas)
        print("Koniec")
        break
    else:
        print("Nie ma takiej mozliwosci, Sprobuj ponownie")
        continue