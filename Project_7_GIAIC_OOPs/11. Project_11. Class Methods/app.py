class Book:
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment count when a new book is created
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    def display_info(self):
        print(f"This Book {self.title} is written by {self.author}")


if __name__ == "__main__":
    book1 = Book("'Python Programming'", "Abdullah")
    book2 = Book("'Data Science'", "Ali")
    book3 = Book("'Machine Learning'", "Ahmed")
    
    # Display book information
    print("Book Information:")
    book1.display_info()
    book2.display_info()
    book3.display_info()
    
    # Display total number of books
    print(f"\nTotal number of books: {Book.get_total_books()}") 