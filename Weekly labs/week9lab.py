# Step 1: Define the Book class
class Book:
    # Step 2: Define __init__ method
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Step 3: Define display_details method
    def display_details(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Pages: ", self.pages)

    # Step 4: Define update_pages method
    def update_pages(self, new_pages):
        self.pages = new_pages
        print(f"The page count for '{self.title}' has been updated to {self.pages} pages.")

# Step 5: Main program
if __name__ == "__main__":
    # Step 6: Create instances of the Book class
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book2 = Book("1984", "George Orwell", 328)

    # Step 7: Display original book details
    print("Original Book Details:")
    book1.display_details()
    print()
    book2.display_details()

    # Step 8: Update the page count of each book
    print("Updating Page Count:")
    book1.update_pages(300)
    book2.update_pages(350)

    # Step 9: Display updated book details
    print("Updated Book Details:")
    book1.display_details()
    book2.display_details()