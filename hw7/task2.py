# Створіть програму, яка емулює роботу сервісу зі скорочення посилань.
# Повинна бути реалізована можливість введення початкового посилання та короткої назви і отримання початкового посилання за її назвою.

links = [
    {
        "link": "https://www.google.com/",
        "short_name": "google"
    }
]

user_answer = input("Insert link or link name: ")

for i in links:
    if user_answer == "https://www.google.com/":
        print(i["short_name"])
    if user_answer == "google":
        print(i["link"])
