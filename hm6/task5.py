# Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list.
# Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list, repeat кількість разів. Очистіть список int_list.
#
int_list = [45, 124, 56, 13, 78, 97, 32, 134, 56, 78, 11, 23, 55, 679]
new_list = []

for i in int_list:
    if i % 2 == 1:
        new_list.append(i)
print(new_list)

repeat = int(input("Insert number of repeats: "))
repeat_list = []

for k in range(repeat):
    repeat_list = new_list.copy() * k
print(repeat_list)

int_list.clear()


