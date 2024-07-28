# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу, і функцію продажу заданого
# автомобіля.


class Auto:
    counter = 0

    def __init__(self, brand):
        self.brand = brand
        self.__class__.counter += 1

    def __str__(self):
        return self.brand


class Salon:

    def __init__(self, salon_name):
        self.salon_name = salon_name
        self.car_list = []

    def list_of_available_cars(self, *args):
        for car in args:
            if isinstance(car, Auto):
                self.car_list.append(car)

    def __str__(self):
        if not self.car_list:
            return "No cars available in the salon."

        # Формує рядок з усіх автомобілів
        car_descriptions = [str(car) for car in self.car_list]  # Викликає __str__ для кожного автомобіля
        return "Available cars:\n" + "\n".join(car_descriptions)

    def sell_car(self, car):
        if car in self.car_list:
            self.car_list.remove(car)


audi = Auto("audi")
bmw = Auto("bwm")
kia = Auto("kia")
lexus = Auto("lexus")
renault = Auto("renault")

kyiv = Salon("Kyiv")
kyiv.list_of_available_cars(audi, bmw, kia, lexus, renault)

print(kyiv)
kyiv.sell_car(audi)
print(kyiv)