def average_in_month(data_base,month,year):
    sum_systolic_pressure=0
    sum_diastolic_pressure=0
    sum_blood_pressure=0
    n=0
    for i in data_base:
        if i[0][3:5]==month and i[0][6:10]==year:
            sum_systolic_pressure+=int(i[1])
            sum_diastolic_pressure+=int(i[2])
            sum_blood_pressure+=int(i[3])
            n+=1
    if n==0:
        print("\nBrak pomiarów w wybranym miesiącu lub wprowadzone dane są niepoprawne\n")
    else:
        average_values = [int(sum_systolic_pressure/n),int(sum_diastolic_pressure/n),int(sum_blood_pressure/n)]
        print("\nŚrednie wartości ciśnienia w miesiącu "+month+"."+year+" to:\nCiśnienie skurczowe - " + str(average_values[0])+\
          "\nCiśnienie rozkurczowe - " + str(average_values[1]) +"\nPuls - " + str(average_values[2])+"\n")
