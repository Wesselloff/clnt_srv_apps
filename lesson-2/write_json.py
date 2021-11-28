"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
   Написать скрипт, автоматизирующий его заполнение данными. Для этого:
       - Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
         цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
         в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
       - Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого
         параметра.
"""

import json


class WriteJson:
    def __init__(self, filename: str):
        self.filename = filename
        with open(filename, 'r', encoding='utf-8') as file:
            self.json_data = json.load(file)
            self.order_lst = self.json_data['orders']

    def add_data(self, item: str, quantity: str, price: str, buyer: str, date: str):
        record = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        self.order_lst.append(record)

    def save(self, name=None):
        if not name:
            name = self.filename
        with open(name, 'w', encoding='utf-8') as file:
            json.dump(self.json_data, file, indent=4, ensure_ascii=False)


FILE_NAME = 'orders.json'

orders = WriteJson(FILE_NAME)
orders.add_data('Монитор', '5', '12000', 'Пупкин Вася', '01.09.2021')
orders.add_data('Системный блок', '1', '57000', 'Какой-то чувак', '25.07.2020')
# Добавляем записи в исходный файл
orders.save()

del orders

orders = WriteJson(FILE_NAME)
orders.add_data('Видеокарта', '15', '89999', 'Майнер Петя', '31.12.2018')
orders.add_data('Коврик для мыши', '2', '57000', 'Маша', '17.03.2015')
orders.add_data('Тапочки для тараканов', '1', '59', 'Шутник', '29.02.2016')
# Сохраняем изменения в новый файл
orders.save("1.json")
