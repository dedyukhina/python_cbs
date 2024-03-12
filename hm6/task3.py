# Простим називається число, яке ділиться націло лише на одиницю і на саме себе. Число 1 не вважається простим.
# Напишіть програму, яка знаходить усі прості числа в заданому проміжку, виводить їх на екран,
# а потім на вимогу користувача виводить їхню суму або добуток.
#

result = []
for i in range(1, 10):

    if i % 2 == 1:
        result.append(i)
print(result)

sum_result = 0
for j in result:
    sum_result += j
print(sum_result)

dobutok = 1
for k in result:
   dobutok *= k
print(dobutok)
