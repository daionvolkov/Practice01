from func import *


user_input = input("Command ('loc', 'zip', 'dist', 'end') => ")
while user_input != 'end':
    if user_input == 'loc':
        try:
            user_input_cmd = int(input('Enter a ZIP Code to lookup => '))
            print(get_loc(user_input_cmd))
        except ValueError:
            print("Введено неверное значение")
        except IndexError:
            print("Значение не найдено")
    if user_input == 'dist':
        try:
            user_input_first_code = int(input('Enter the first ZIP Code => '))
            user_input_second_code = int(input('Enter the first ZIP Code => '))
            print(get_dist(user_input_first_code, user_input_second_code))
        except ValueError:
            print("Введено неверное значение")
        except IndexError:
            print("Значение не найдено")

    if user_input == 'zip':
        try:
            user_input_city = input('Enter a city name to lookup => ').title()
            user_input_state = input(
                'Enter the state name to lookup =>').upper()
            print(get_zip(user_input_city, user_input_state))
        except ValueError:
            print("Введено неверное значение")
        except IndexError:
            print("Значение не найдено")
    user_input = input("Command ('loc', 'zip', 'dist', 'end') => ")
