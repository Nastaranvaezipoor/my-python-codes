#تمرین_شماره_چهارم 
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", int(self.price))
        print("--------------------")

    def apply_discount(self, percent):
        discount_amount = (self.price * percent) / 100
        new_price = self.price - discount_amount
        return new_price

books = [
    Book("Daallan Behesht", "Nazi Safavi", 379000),
    Book("Python Crash Course", "Eric Matthes", 450000)
]

print("Available Books with Details:")
for i in range(len(books)):
    print(f"Book {i+1}:")
    books[i].display_details()

choice_input = input("Select book number (1 or 2): ")
choice = int(choice_input) - 1

percent_input = input("Enter discount percent: ")
percent = float(percent_input)

selected_book = books[choice]
old_price = selected_book.price
new_price = selected_book.apply_discount(percent)

print("\nFinal Results for Selected Book:")
print("Title:", selected_book.title)
print("Author:", selected_book.author)
print("Original Price:", int(old_price))
print("Price After Discount:", int(new_price))
