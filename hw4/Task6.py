# Створіть програму авторизації, в якій користувачеві дається 3 спроби ввести свої облікові дані (логін та пароль).
# Якщо користувач за меншу кількість спроб ввів вірні дані, програма достроково припиняє своє виконання та виводить на екран повідомлення:
# «Авторизацію успішно пройдено з «№» спроби».

login = "ola@gmail.com"
password = "1234!"
for i in range(1, 4):
    user_name = input("Insert your login: ")
    user_password = input("Insert you password: ")
    if user_name == login and user_password == password:
        print("Successful authorization. Try # ", i)
        break
    else:
        print("Not authorized")
