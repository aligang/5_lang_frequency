## 1.Что это такое ?

Этот код позволяет найти 10 самых повторяющихся слов в тексте

## 2.Системные требования
Для работы с программой понадобится Python3.5 (который скорее всего у вас уже установлен, если Вы используете Linux)  


## 3.Где можно скачать  
Можно форкнуть здесь - [частота слов](https://github.com/aligang/5_lang_frequency)  
и затем скачать 
```
git clone https://github.com/<юзернейм-аккаунта-на-гите>/5_lang_frequency
```

## 4.Как этим пользоваться...  
*a.Данный код может быть исползован как самостоятельная программа,*  
*при этом в качестве аргумента нужно будет указать путь до файла, текст из которого нужно будет обработать*

```bash
# python3 lang_frequency.py text.txt 

Cамые часто повторяющиеся слова в файле text.txt

Слово                      встречается раз(a)
и ............................. 4
в ............................. 4
на ............................ 4
xp ............................ 2
к ............................. 4
компьютер ..................... 2
сервера ....................... 2
данных ........................ 3
порты ......................... 2
mediawiki ..................... 3
```

## 5.Какие функции могут быть переиспользованы в вашем коде
Функция `load_data` считывает содержимое файла в одну строку  
Функция `get_most_frequent_words` принимает на вход строку и выдаёт плоский словарь 
формата (слово: кол-во повторений в тексте)
Функция `print_pretty_output` выводит словарь, полученный на выходе функции `get_most_frequent_words`,
на поток ввода-вывода 

Импортировать и использовать функцию коди можно  следующим образом:  
```python
from lang_frequency import load_data
from lang_frequency import get_most_frequent_words


text_from_file = load_data(textfile_path)
most_frequent_words = get_most_frequent_words(text_from_file)
```

## 6. Цели
Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)