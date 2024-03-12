# Створіть цілочисельний список, введіть кількість його елементів і самі значення.
# Передбачити меню, в якому: після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку,
# а після натискання клавіші 2 – за зростанням.
#

numbers = [34, 78, 49, 22, 11, 406, 89, 124, 5, 6, 9, 3, 40, 30, 66, 74, 92, 205, 632, 294, 581, 345]
print(numbers)
print(len(numbers))

while True:
    user_click = int(input("Insert 1 or 2 : "))
    if user_click == 1:
        numbers.reverse()
        print(numbers)
    if user_click == 2:
        numbers.sort()
        print(numbers)

