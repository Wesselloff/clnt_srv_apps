"""
    4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
       в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

STRING_LST = ['разработка', 'администрирование', 'protocol', 'standard']

bytes_str = [i.encode('utf-8') for i in STRING_LST]
print(bytes_str)

string_str = [i.decode('utf-8') for i in bytes_str]
print(string_str)
