"""
    6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
       «сетевое программирование», «сокет», «декоратор».
       Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect

FILE_NAME = 'test_file.txt'
STRING_LST = ['сетевое программирование', 'сокет', 'декоратор']


def create_file(name: str, lines: list):
    with open(name, 'w') as file:
        for i in lines:
            file.write(f'{i}\n')


def convert_file(name: str):
    with open(name, 'rb') as file:
        file_bytes = file.read()
    file_text = file_bytes.decode(detect(file_bytes)['encoding'])
    with open(name, 'w', encoding='utf-8') as file:
        file.write(file_text)


create_file(FILE_NAME, STRING_LST)
convert_file(FILE_NAME)

with open(FILE_NAME, 'r', encoding='utf-8') as file:
    lines = file.read()

print(lines)
