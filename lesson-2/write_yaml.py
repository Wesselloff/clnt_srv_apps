"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
   YAML-формата. Для этого:
       - Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму —
         целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
         отсутствующим в кодировке ASCII (например, €);
       - Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
         файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом:
         allow_unicode = True;
       - Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

menu = {'food': ['sausage', 'butter', 'bread', 'potato', 'Fanta'],
        'count': 5,
        'prices': {'sausage': '10\u20ac',
                   'butter': '20\u20ac',
                   'bread': '1\u20ac',
                   'potato': '4\u20ac',
                   'Fanta': '5\u20ac'
                   }
        }

with open('file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(menu, file, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as file:
    loaded_menu = yaml.load(file, Loader=yaml.SafeLoader)

if menu == loaded_menu:
    print('Данные совпадают')
else:
    print('Данные различаются')
