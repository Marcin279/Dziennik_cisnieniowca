from os import path

def load_data_base(data_base):
    if path.exists("./DC_baza_danych.txt")==1:
        file=open("./DC_baza_danych.txt", 'r')
    else:
        file=open("./DC_baza_danych.txt", 'x')
        file.close()
        file=open("./DC_baza_danych.txt", 'r')
    
    for line in file:
        if line!='':
            data_base.append(line.split())
    file.close()

def save_data_base(new_datas):
    file=open("./DC_baza_danych.txt", 'a')
    to_save = ""
    if new_datas!=0:
        for i in new_datas:
            to_save=to_save+i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\n'
    file.write(to_save)
    file.close()
