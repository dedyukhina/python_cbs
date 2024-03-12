# import math
# # 1
# fist_name = input('Input your first name : ')
# if fist_name == 'Oleksandra':
#     print('Wow! We have the same name')
# else: print('Nice to meet you!')
#
#
# # 2
# # --------
#
# # 3
# # ---------
#
# # 4
# action = input(
#     'Виберіть операцію: додавання, віднімання, множення, ділення, зведення в ступінь, квадратний корінь, кубічний корінь, синус, косинус та тангенс числа ')
#
# if action == 'додавання':
#     num_1 = int(input('Внесіть перше число: '))
#     num_2 = int(input('Внесіть друге число: '))
#     num_sum = num_1 + num_2
#     print("Результат =  " + str(num_sum))
# elif action == 'віднімання':
#     num_1 = int(input('Внесіть перше число: '))
#     num_2 = int(input('Внесіть друге число: '))
#     num_minus = num_1 - num_2
#     print("Результат =  " + str(num_minus))
# elif action == 'множення':
#     num_1 = int(input('Внесіть перше число: '))
#     num_2 = int(input('Внесіть друге число: '))
#     num_multiple = num_1 * num_2
#     print("Результат =  " + str(num_multiple))
# elif action == 'ділення':
#     num_1 = int(input('Внесіть перше число: '))
#     num_2 = int(input('Внесіть друге число: '))
#     num_divide = num_1 / num_2
#     print("Результат =  " + str(num_divide))
# elif action == 'зведення в ступінь':
#     num_1 = int(input('Внесіть перше число: '))
#     num_2 = int(input('Внесіть друге число: '))
#     num_exponentiation = num_1 ** num_2
#     print("Результат =  " + str(num_exponentiation))
# elif action == 'квадратний корінь':
#     num_1 = int(input('Внесіть число: '))
#     num_sqr_root = math.sqrt(num_1)
#     print("Результат =  " + str(num_sqr_root))
# elif action == 'кубічний корінь':
#     num_1 = int(input('Внесіть число: '))
#     num_cubic_root = pow(num_1, 1 / 3)
#     print("Результат =  " + str(num_cubic_root))
# elif action == 'синус':
#     num_1 = int(input('Внесіть число в градусах: '))
#     num1_in_radians = math.radians(num_1)
#     num_sinus = math.sin(num1_in_radians)
#     print("Результат =  " + str(num_sinus))
# elif action == 'косинус':
#     num_1 = int(input('Внесіть число в радіанах: '))
#     num_cosinus = math.cos(num_1)
#     print("Результат =  " + str(num_cosinus))
# elif action == 'тангенс числа':
#     num_1 = int(input('Внесіть число в градусах: '))
#     num1_in_radians = math.radians(num_1)
#     num_tangens = math.tan(num1_in_radians)
#     print("Результат =  " + str(num_tangens))
# else:
#     print('Немає такої дії. Спробуйте ще раз!')

#5
#
# number = int(input('Введіть число: '))
# result = 'парне' if number % 2 == 0 else 'непарне'
# print('Введене число є ' + str(result))

#6

# day = input('Введіть день тижня: ')
# match day:
#     case 'Понеділок':
#         print('Сьогодні на роботу')
#     case 'Вівторок':
#         print('Сьогодні на роботу')
#     case 'Середа':
#         print('Сьогодні на роботу')
#     case 'Четвер':
#         print('Сьогодні на роботу')
#     case 'Пятнция':
#         print('Сьогодні на роботу')
#     case 'Субота':
#         print('Сьогодні вихідний')
#     case 'Неділя':
#         print('Сьогодні вихідний')
#     case _:
#         print('Такого дня не існує')
#
# 6.v2
# day = input('Введіть день тижня: ')
#
# if day == 'Понеділок' or day == 'Вівторок' or day == 'Середа' or day == 'Четвер' or day == 'Пятниця':
#     print('Сьогодні вихідний')
# else:
#     print('Такого дня не існує')










