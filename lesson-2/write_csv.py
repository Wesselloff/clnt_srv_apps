"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
   info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
       - Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
         считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
         значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого
         параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list,
         os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных
         отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
         «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
         Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
       - Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
         получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий
         CSV-файл;
       - Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re
from chardet import detect


class WriteCsv:
    def __init__(self, files: list):
        self.file_list = files
        self.main_data = []
        self.os_prod_list = []
        self.os_name_list = []
        self.os_code_list = []
        self.os_type_list = []
        self.header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
        self.prod_ptrn = re.compile(r'Изготовитель системы:\s*(.*)')
        self.name_ptrn = re.compile(r'Название ОС:\s*(.*)')
        self.code_ptrn = re.compile(r'Код продукта:\s*(.*)')
        self.type_ptrn = re.compile(r'Тип системы:\s*(.*)')

    def get_data(self):
        for i in self.file_list:
            with open(i, 'rb') as file:
                data = file.read()
                data = data.decode(detect(data)['encoding'])
                self.os_prod_list.append(self.prod_ptrn.search(data).group(1).strip('\n\r '))
                self.os_name_list.append(self.name_ptrn.search(data).group(1).strip('\n\r '))
                self.os_code_list.append(self.code_ptrn.search(data).group(1).strip('\n\r '))
                self.os_type_list.append(self.type_ptrn.search(data).group(1).strip('\n\r '))
        self.main_data.append(self.header)
        for i in range(len(self.os_prod_list)):
            self.main_data.append([self.os_prod_list[i],
                                   self.os_name_list[i],
                                   self.os_code_list[i],
                                   self.os_type_list[i]])

    def write_to_csv(self, filename: str):
        self.get_data()
        with open(filename, 'w', encoding='utf-8') as file:
            csv_file = csv.writer(file)
            for i in self.main_data:
                csv_file.writerow(i)


file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
OUT_FILE = 'main_data.csv'

os_data = WriteCsv(file_list)
os_data.write_to_csv(OUT_FILE)
