Funkcjonalność reprezentuje klasa "AddNewPosition". Metoda inicjalizująca klasę (Konstruktor) posiada 4 parametry:
-> date(data),
-> systolic_pressure(ciśnienie skurczowe),
-> diastolic_pressure(ciśnienie rozkurczowe),
-> blood_pressure(ciśnienie tętnicze).

Klasa posiada "AddNewPosition" posiada metodę "add", która zwraca powyższe parametry w formie listy: [date, systolic_pressure, diastolic_pressure, blood_pressure]

Przykład działania:


lista1 = AddNewPosition("12.02.2020", 145, 74, 76)

lista2 = AddNewPosition("12.02.2026", 135, 76, 56)

listaglowna = [lista1.add(), lista2.add()]

print(listaglowna)

Wynik działania:

[['12.02.2020', 145, 74, 76], ['12.02.2026', 135, 76, 56]]
