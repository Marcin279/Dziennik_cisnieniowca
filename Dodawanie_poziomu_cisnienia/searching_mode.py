from file_mode import data_unpack


def search_by_date():
    temp_list = []
    searching_date = input("Podaj date [dzien.miesiac.rok]:  ")
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
