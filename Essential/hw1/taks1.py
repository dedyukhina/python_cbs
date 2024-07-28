class Book:
    def __init__(self, author, name, year, genre):
        self.genre = genre
        self.year = year
        self.name = name
        self.author = author
        self.reviews = []

    def add_review_to_book(self, review):
        self.reviews.append(review)
    def __str__(self):
        reviews_str = "\n".join(str(review) for review in self.reviews)
        return (f"Author: {self.author}, Name: {self.name}, Year: {self.year}, Genre: {self.genre}, "
                f"Reviews:\n{reviews_str if reviews_str else 'No reviews yet.'}")

    def __repr__(self):
        return f"Author of the book: {self.author}, Name: {self.name}, Year: {self.year}, Genre: {self.genre}"


class BookReview:
    def __init__(self, review):
        self.review_list = []
        self.review_list.append(review)

    def __str__(self):
        return f"{self.review_list}"


book_1 = Book("j.k.rowling", "harry potter", 1999, "fiction")
book_2 = Book("Simon Becket", "Hunter", 2006, "fiction")
review1 = BookReview("jkfjsfksjkdf")
book_1.add_review_to_book(review1)
print(book_1)