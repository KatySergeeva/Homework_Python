from book import Book

library = [
    Book("Sheep's hunting", "Haruki Murakami"),
    Book("The Hunger Games", "Suzanne Collins"),
    Book("Alice in Wonderland", "Lewis Carroll")
]
for book in library:
    print(f"{book.name} - {book.autor}")