# Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5.
# Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів та його позицію у цьому списку.
#


new_list = [45, 13, 97, 11, 23, 55, 679, 45, 13, 97, 11, 23, 55, 679, 45, 13, 97, 11, 23, 55, 679, 45, 13, 97, 11, 23,
            55, 679]

user_number = int(input("Insert your number: "))

for i in new_list:
    if user_number == i:
        user_number = i
print(new_list.count(user_number))
print(new_list.index(user_number))


