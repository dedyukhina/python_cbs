from collections import defaultdict
from operator import itemgetter

# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою:
# автор: твір. Передбачте можливість виведення на екран сортування за автором та твором.
#
books = []
n = int(input("How many books you want to add? "))

for i in range(n):
    author = input("Insert author: ")
    book = input("Insert book: ")
    books.append({"author": author, "book": book})

sort_option = input("Do you want to sort by author or by book? ")

if sort_option == "author":
    sorted_authors = sorted(books, key=itemgetter("author"))
    print(sorted_authors)
elif sort_option == "book":
    sorted_books = sorted(books, key=itemgetter("book"))
    print(sorted_books)
else:
    print("Invalid")
