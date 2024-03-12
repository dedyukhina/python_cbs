# Створіть список та введіть його значення. Знайдіть найбільший та найменший елемент списку, а також суму та середнє арифметичне його значень.
#
numbers = [5, 10, 26, 105, 1, 0, 125, 678, 7]
numbers.sort()
min_number = numbers[0]
max_number = numbers[-1]
sum_numbers = 0

for i in numbers:
    sum_numbers += i
print(sum_numbers)

avg = sum_numbers / len((numbers))
print(avg)
