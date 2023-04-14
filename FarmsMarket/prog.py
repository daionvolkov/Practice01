from FarmersMarket import *
import pandas as pd
import sqlite3
from geopy.distance import geodesic


if __name__ == '__main__':
    db_file = 'farmers_market.db'
    csv_file = 'Export.csv'
    fm = FarmersMarket(db_file, csv_file)
    # fm.load_data()
    # fm.view_all(1)
    # fm.search_by_city_state('New York', 'NY', 30)
    # fm.search_by_zip('10001', 30)
    # fm.view_details(1018318)


# fm = FarmersMarket('farmers_market.db', 'Export.csv')
# fm.load_data()
# fm.view_all(1)
# fm.search_by_city_state('New York', 'NY', 30)
# fm.search_by_zip('10001', 30)
# fm.view_details(1018318)

while (True):
    print(f'Показать список всех фермерских рынков в стране нажмите:', f'1')
    print(f'Выполнить поиск по городу и штату, радиусу нажмите:', f'2'.rjust(6))
    print(f'Выполнить поиск индексу, радиусу нажмите:', f'3'.rjust(16))
    print(f'Выполнить поиск информации по id нажмите:', f'4'.rjust(16))
    print('для выхода: 0')
    try:
        user_input = int(input())
    except ValueError:
        print('неверый ввод')
    if user_input == 1:
        input_columns = input(
            'Какие столбцы вывести, через запятую: ').split(',')
        fm.load_data()
        fm.view_all(2, input_columns)
        break
    if user_input == 2:
        input_city = input('Введите город: ')
        input_state = input('Введите штат: ')
        input_radius = input('Введите радиус поиска: ')
        print(fm.search_by_city_state(input_city, input_state, input_radius))
    if user_input == 3:
        input_zip = int(input('Введите индекс: '))
        input_radius = int(input('Введите радиус поиска: '))
        print(fm.search_by_zip(input_zip, input_radius))
    if user_input == 4:
        try:
            input_fmid = int(input('Введите id: '))
            fm.view_details(input_fmid)
        except ValueError:
            print('Неверный ввод')
    if user_input == 0:
        break
    else:
        print('Неверный ввод')
