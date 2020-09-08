import urllib.request
from inscriptis import get_text
import codecs
import time
#подключаем библиотеки

url = input('Введите URL нужной страницы :')
time.sleep(2)
print('Спасибо, идёт парсинг выбраной страницы')
time.sleep(4)
html = urllib.request.urlopen(url).read().decode('utf-8')        #cоздаем переменные для ввода сыылки на сайт и для ее чтения

text = get_text(html)       #получаем текст с веб-страницы
print(text)                 #выводим текст в терминал
f = codecs.open("myfile.txt", "w", "utf-8")  #открываем файл и читаем его кодировку
f.writelines(text) #записываем в этот файл текст с сайта
Lines = f.readline   #читаем наш файл
f.close()
time.sleep(5)
print('\n\nЕще читаем...')
time.sleep(3)
print('\n\n\nФайл прочитан, программа завершена')