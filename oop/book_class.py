class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for the book (user-friendly)."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the book, useful for debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
