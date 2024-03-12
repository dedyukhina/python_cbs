# Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами
# - унікальними словами та значеннями - кількістю повторів кожного слова у послідовності.
#


string = ("Each lesson preparation task reading text and two tasks  check your understanding and  practise a variety "
          "of reading skills"
          "Make  start today Each lesson preparation task reading text and two tasks  check your understanding and  "
          "practise a variety of reading skills"
          "Make  start today Each lesson preparation task reading text and two tasks  check your understanding and  "
          "practise a variety of reading skills"
          "Make  start today Each lesson preparation task reading text and two tasks  check your understanding and  "
          "practise a variety of reading skills  Make  start today")

words = string.split()
my_list = list(words)

new_dict = {}

for i in my_list:
    key = i
    value = my_list.count(i)
    new_dict.update({key: value})
print(new_dict)


