names = ["Alex", "Daria", "Oleg", "Victoria", "Oleksandra", "Dmitro"]
ages = [19, 45, 67, 80, 43, 24]
married = [True, True, False, True, False, False]

# def convertor():
#     new_dict = {}
#     for i in range(len(names)):
#         name = names[i]
#         new_dict[i] = {"name": name}
#     for k in range(len(ages)):
#         age = ages[k]
#         new_dict[k] = {"age": age}
#
#
# """
# Треба зробити так, щоб кожен елемент списку перетворився на обʼєкт з даними з сусіднього списку;
# список, всередині якого будуть обʼєкти з даних
#
# :return: [{"name": "Alex", "age": 19, "married": True}, {"name": "Daria", "age": 45, "married": True}, ...]
# """
#
# print(convertor())

names = ["Alex", "Daria", "Oleg", "Victoria", "Oleksandra", "Dmitro"]
ages = [19, 45, 67, 80, 43, 24]
married = [True, True, False, True, False, False]
bycicles = [True, True, True, True, False, True]


def convertor(**data):
    """
    Треба зробити так, щоб кожен елемент списку перетворився на обʼєкт з даними з сусіднього списку;
    список, всередині якого будуть обʼєкти з даних

    :return: [{"name": "Alex", "age": 19, "married": True}, {"name": "Daria", "age": 45, "married": True}, ...]
    """
    return [{key: value} for key, value in data.items()]


print(convertor(names))
