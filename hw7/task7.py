# Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до структури(реалізуйте інтерфейс(меню), за допомогою якого можна робити маніпуляції з даними):
#
# прізвище:
#
#     посада: ...
#
#     досвід роботи: …
#
#     портфоліо: …
#
#     коефіцієнт ефективності: …
#
#     стек технологій: …
#
#     зарплата: …
#
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.
from operator import itemgetter

employees = {}
n = int(input("How many employess to add?: "))
for i in range(n):
    surname = input("surname: ")
    role = input("role: ")
    experience = int(input("experience in months: "))
    portfolio = input("link to portfolio: ")
    kpi = int(input("kpi: "))
    stek = input("stek: ")
    salary = input("salary: ")
    employees[i] = {"surname": surname, "role": role, "experience": experience, "portfolio": portfolio, "kpi": kpi,
                    'stek': stek, "salary": salary}

action = input("what to do? (display, sort by surname, sort by kpi): ")
match action:
    case "display":
        print(employees)
    case "sort by surname":
        sort_by_surname = sorted(employees, key=itemgetter(1, "surname"))
        print(sort_by_surname)
    case "sort by kpi":
        sort_by_kpi = sorted(employees, key=itemgetter(1, "kpi"))
        print(sort_by_kpi)
