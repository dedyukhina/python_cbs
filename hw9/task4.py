# Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.
#
def sum_of_numbers(start, end):
    if start > end:
        return 0
    else:
        return start + sum_of_numbers(start + 1, end)

print(sum_of_numbers(1, 10))
