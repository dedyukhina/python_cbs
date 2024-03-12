# Створіть функцію, яка відображає привітання для користувача із заданим ім'ям.
# Якщо ім'я не вказано, вона повинна виводити привітання для користувача з Вашим ім'ям.
#

def greetings():
    default_name = "Oleksandra"
    user_name = input("insert your name: ")
    if user_name:
        print("Hi,", user_name)
    else:
        print("Hi", default_name)

greetings()