# Є два списки, які наповнюються користувачем з клавіатури.
# Сформувати список, в якому будуть міститися унікальні значення першого відносно другого списку
# та навпаки без повторень. Роздрукувати підсумковий об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.

first_numbers = list(input())
second_numbers = list(input())
first_to_second_numbers = set(first_numbers) - set(second_numbers)
second_to_fist_numbers = set(second_numbers) - set(first_numbers)
third_list_numbers = list(first_to_second_numbers) + list(second_to_fist_numbers)
print(third_list_numbers)
third_list_numbers.reverse()
print(third_list_numbers)
third_list_numbers.sort()
print(third_list_numbers)
third_list_numbers.sort(reverse=True)
print(third_list_numbers)

