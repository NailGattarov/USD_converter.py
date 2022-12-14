import requests

# Берем курсы валют с сайта openexchangerates.org
data = requests.get('https://openexchangerates.org/api/latest.json?app_id=f02103aa3e3a4f58ba88e926982a32d0').json()
USD_RUB_rate = data['rates']['RUB']
USD_UZS_rate = data['rates']['UZS']
USD_GEL_rate = data['rates']['GEL']

# Выводим курсы валют на сегодня
print('Курс доллара на сегодняшний день:')
print('\033[34m {} рублей'.format(round(USD_RUB_rate, 2)))
print(' {0:,} сум'.format(round(USD_UZS_rate, 2)).replace(',', ' '))
print(' {} лари\033[0m'.format(round(USD_GEL_rate, 2)))
print('Сколько у вас есть долларов?')

# Просим пользователя ввести количество долларов для обмена
USD_count = None
while True:
    try:
        USD_count = float(input())
    except ValueError:
        print('\033[31mИзвините, я вас не понял. Пожалуйста, введите число и повторите попытку\033[0m')
        continue
    else:
        break
if USD_count <= 1000:
    print('\033[33mНе так уж и много, но тоже неплохо.\033[0m')
else:
    print('\033[33mНеплохо, на iphone может и хватит.\033[0m')

# Вычисления
RUB_count_int = int(USD_RUB_rate * USD_count)
RUB_count_round = round(USD_RUB_rate * USD_count, 2)
kop_count = int(round((RUB_count_round - RUB_count_int) * 100))

# Используем это в помощь для определения склонения названия валюты
one_last_digit_ruble = int(str(RUB_count_int)[-1])
try:
    two_last_digits_ruble = int(str(RUB_count_int)[-2:])
except IndexError:
    two_last_digits_ruble = int(0 + one_last_digit_ruble)

one_last_digit_kop = int(str(kop_count)[-1])
try:
    two_last_digits_kop = int(str(kop_count)[-2:])
except IndexError:
    two_last_digits_kop = int(0 + one_last_digit_kop)

UZS_count_int = int(USD_UZS_rate * USD_count)
UZS_count_round = round(USD_UZS_rate * USD_count, 2)
tiin_count = int(round((UZS_count_round - UZS_count_int) * 100))

one_last_digit_sum = int(str(UZS_count_int)[-1])
try:
    two_last_digits_sum = int(str(UZS_count_int)[-2:])
except IndexError:
    two_last_digits_sum = int(0 + one_last_digit_sum)

one_last_digit_tiin = int(str(tiin_count)[-1])
try:
    two_last_digits_tiin = int(str(tiin_count)[-2:])
except IndexError:
    two_last_digits_tiin = int(0 + one_last_digit_tiin)

GEL_count_int = int(USD_GEL_rate * USD_count)
GEL_count_round = round(USD_GEL_rate * USD_count, 2)
tetri_count = int(round((GEL_count_round - GEL_count_int) * 100))

list1 = [0, 5, 6, 7, 8, 9]
list2 = [1]
list3 = [11]
list4 = [2, 3, 4]
list5 = [12, 13, 14]


# Функции для определения склонения названия валюты
def ruble_name():
    if one_last_digit_ruble in list1:
        return 'рублей'
    if one_last_digit_ruble in list2:
        if one_last_digit_ruble in list3:
            return 'рублей'
        return 'рубль'
    if one_last_digit_ruble in list4:
        if two_last_digits_ruble in list5:
            return 'рублей'
        return 'рубля'


def kop_name():
    if one_last_digit_kop in list1:
        return 'копеек'
    if one_last_digit_kop in list2:
        if two_last_digits_kop in list3:
            return 'копеек'
        return 'копейку'
    if one_last_digit_kop in list4:
        if two_last_digits_kop in list5:
            return 'копеек'
        return 'копейки'


def sum_name():
    if one_last_digit_sum in list1:
        return 'сумов'
    if one_last_digit_sum in list2:
        if one_last_digit_sum in list3:
            return 'сумов'
        return 'сум'
    if one_last_digit_sum in list4:
        if two_last_digits_sum in list5:
            return 'сумов'
        return 'сума'


def tiin_name():
    if one_last_digit_tiin in list1:
        return 'тийинов'
    if one_last_digit_tiin in list2:
        if two_last_digits_tiin in list3:
            return 'тийинов'
        return 'тийин'
    if one_last_digit_tiin in list4:
        if two_last_digits_tiin in list5:
            return 'тийинов'
        return 'тийина'


# Выводим результат
print('За ваши доллары вы получите:')
print('\033[34m {0:,}'.format(RUB_count_int).replace(',', ' '), ruble_name(), kop_count, kop_name())
print(' {0:,}'.format(UZS_count_int).replace(',', ' '), sum_name(), tiin_count, tiin_name())
print(' {0:,} лари'.format(GEL_count_int).replace(',', ' '), tetri_count, 'тетри\033[0m')
