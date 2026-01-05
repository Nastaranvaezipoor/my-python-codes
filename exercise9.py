#تمرین_شماره_نهم
import tkinter as tk
from tkinter import messagebox
import os

class Contact:
    def init(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits.")
        self.name = name
        self.phone_number = phone_number

class PhoneBookApp:
    def init(self, root):
        self.root = root
        self.root.title("PhoneBook")
        self.contacts = []
        self.filename = "contacts.csv"

        self.load_from_csv()

        tk.Label(root, text="Search:").grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(root, text="Search", command=self.search_contact).grid(row=0, column=2, padx=5, pady=5)

        self.listbox = tk.Listbox(root, width=40)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.listbox.bind('<Return>', self.show_selected_phone)

        tk.Label(root, text="Name:").grid(row=2, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=1)

        tk.Label(root, text="Phone:").grid(row=3, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=3, column=1)

        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=1, pady=5)
        
        tk.Button(root, text="Delete", command=self.delete_contact, fg="red").grid(row=5, column=0, pady=10)
        tk.Button(root, text="Show Number", command=self.show_selected_phone, bg="lightblue").grid(row=5, column=1, pady=10)
        tk.Button(root, text="Exit", command=self.exit_app, bg="gray").grid(row=5, column=2, pady=10)

        self.update_listbox(self.contacts)

    def update_listbox(self, data_list):
        self.listbox.delete(0, tk.END)
        for c in data_list:
            self.listbox.insert(tk.END, c.name)

    def show_selected_phone(self, event=None):
        try:
            selection = self.listbox.curselection()
            if selection:
                index = selection[0]
                selected_name = self.listbox.get(index)
                for c in self.contacts:
                    if c.name == selected_name:
                        self.name_entry.delete(0, tk.END)
                        self.name_entry.insert(0, c.name)
                        self.phone_entry.delete(0, tk.END)
                        self.phone_entry.insert(0, c.phone_number)
                        break
        except Exception:
            pass

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            try:
                new_contact = Contact(name, phone)
                self.contacts.append(new_contact)
                self.update_listbox(self.contacts)
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def search_contact(self):
        query = self.search_entry.get().lower()
        if not query:
            self.update_listbox(self.contacts)
            return

        results = [c for c in self.contacts if query in c.name.lower()]
        if not results:
            messagebox.showinfo("Search Result", "Contact not found!")
            self.update_listbox(self.contacts)
        else:
            self.update_listbox(results)

    def delete_contact(self):
        try:
            selection = self.listbox.curselection()
            if selection:
                index = selection[0]
                del self.contacts[index]
                self.update_listbox(self.contacts)
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
        except Exception:
            pass

def save_to_csv(self):
        with open(self.filename, "w") as f:
            for c in self.contacts:
                line = str(c.name) + "," + str(c.phone_number) + "\n"
                f.write(line)

    def load_from_csv(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            try:
                self.contacts = []
                with open(self.filename, "r") as f:
                    for line in f:
                        if "," in line:
                            name, phone = line.strip().split(",")
                            self.contacts.append(Contact(name, phone))
            except Exception:
                pass
        
        if not self.contacts:
            self.contacts = [Contact("Sadjad", "36029000"), Contact("Police", "110")]

    def exit_app(self):
        self.save_to_csv()
        self.root.destroy()

if name == "main":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_app)
    root.mainloop()
