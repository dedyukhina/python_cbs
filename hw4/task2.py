n = int(input("Insert your number: "))
factorial = n

while n > 1:
    n -= 1
    factorial *= n
print(factorial)
