"""
    3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

STRING_LST = ['attribute', 'класс', 'функция', 'type']

for i in STRING_LST:
    try:
        eval(f"b'{i}'")
    except SyntaxError:
        print(f'Слово "{i}" невозможно записать в байтовом типе')
