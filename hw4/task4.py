a = int(input("Insert first number: "))
b = int(input("Insert second number: "))
avg = (a + b) / 2
numers_sum = 0

for i in range(a, b, +1):
        if i % avg == 0:
            numers_sum += i
print(numers_sum)



