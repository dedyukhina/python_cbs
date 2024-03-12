# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

word = input("input a word: ")


def palindrome():
    return word == word[::-1]


if palindrome():
    print("palindrome")
else:
    print("not palindrome")
