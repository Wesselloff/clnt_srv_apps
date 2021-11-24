"""
    5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
       на кириллице.
"""

from platform import system
from subprocess import Popen, PIPE
from chardet import detect

URL_LST = ['yandex.ru', 'youtube.com']
REPEAT_CNT = '4'
PING_PARAM = '-n' if system() == 'Windows' else '-c'

for i in URL_LST:
    args = ['ping', PING_PARAM, REPEAT_CNT, i]
    ping_out = Popen(args, stdout=PIPE)
    for s in ping_out.stdout:
        res = detect(s)
        print(res)
        line = s.decode(res['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

