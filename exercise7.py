#تمرین_شماره_هفتم
class Contact:
    def __init__(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("shomare telephone bayad faghat adad bashad")
        self.name = name
        self.phone_number = phone_number

class PhoneBook:
    def __init__(self):
        self.contacts = [
            Contact("Sadjad University", "36029000"),
            Contact("Police", "110"),
            Contact("Emergency", "115"),
            Contact("Taxi", "133")
        ]

    def add_contact(self, name, phone):
        try:
            new_contact = Contact(name, phone)
            self.contacts.append(new_contact)
            print("Mokhatab ezafe shod.")
        except ValueError as e:
            print(f"Error: {e}")

    def save_to_csv(self, filename):
        with open(filename, "w") as f:
            for c in self.contacts:
                f.write(f"{c.name},{c.phone_number}\n")
        print("Zakhire shod.")

    def load_from_csv(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    try:
                        name, phone = line.strip().split(",")
                        self.contacts.append(Contact(name, phone))
                    except:
                        continue
            print("your choice is loaded.")
        except FileNotFoundError:
            print("Welcome\nHere is your phone book:")

my_book = PhoneBook()
my_book.load_from_csv("contacts.csv")

while True:
    print("\n1. add members")
    print("2. show all")
    print("3. save and show")
    
    try:
        choice = input("Enter choice: ")
        
        if choice == "1":
            n = input("Name: ")
            p = input("Phone: ")
            my_book.add_contact(n, p)
            
        elif choice == "2":
            print("\n--- Contacts List ---")
            for c in my_book.contacts:
                print(f"Name: {c.name} | Phone: {c.phone_number}")
                
        elif choice == "3":
            my_book.save_to_csv("contacts.csv")
            print("Good Luck!")
            break
        else:
            print("Enter number between 1 and 3.")
            
    except Exception:
        print("Error!")
