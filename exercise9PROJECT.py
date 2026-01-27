import tkinter as tk
import os

class Contact:
    def __init__(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("Phone number must be digits!")
        self.name = name
        self.phone_number = phone_number

class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PhoneBook Professional")
        self.contacts = []
        self.filename = "contacts.csv"

        self.load_from_csv()

        padding_options = {'padx': 5, 'pady': 5}

        tk.Label(root, text="Search:").grid(row=0, column=0, sticky="w", **padding_options)
        self.search_entry = tk.Entry(root, width=20)
        self.search_entry.grid(row=0, column=1, **padding_options)
        tk.Button(root, text="Go", command=self.search_contact, width=5).grid(row=0, column=2, **padding_options)

        self.listbox = tk.Listbox(root, width=40, height=12)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.show_selected_phone)

        tk.Label(root, text="Name:").grid(row=2, column=0, sticky="w", **padding_options)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=2, column=1, columnspan=2, sticky="w", **padding_options)

        tk.Label(root, text="Phone:").grid(row=3, column=0, sticky="w", **padding_options)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=3, column=1, columnspan=2, sticky="w", **padding_options)

        btn_frame = tk.Frame(root)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=10)

        tk.Button(btn_frame, text="Add", command=self.add_contact, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit", command=self.update_contact, width=10, bg="lightgreen").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Del", command=self.delete_contact, width=10, fg="red").pack(side=tk.LEFT, padx=5)

        tk.Button(root, text="Sort A-Z", command=self.sort_contacts, width=12).grid(row=5, column=0, pady=5)
        tk.Button(root, text="Exit", command=self.exit_app, width=25, bg="gray").grid(row=5, column=1, columnspan=2, pady=5)

        self.status_label = tk.Label(root, text="", fg="red", font=("Arial", 9))
        self.status_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=10)

        self.update_listbox(self.contacts)

    def set_status(self, message, color="red"):
        self.status_label.config(text=message, fg=color)
        self.root.after(4000, lambda: self.status_label.config(text=""))

    def update_listbox(self, data_list):
        self.listbox.delete(0, tk.END)
        for c in data_list:
            self.listbox.insert(tk.END, c.name)

    def sort_contacts(self):
        self.contacts.sort(key=lambda x: x.name.lower())
        self.update_listbox(self.contacts)
        self.set_status("List sorted alphabetically.", "blue")

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
        except: pass

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if not name or not phone:
            self.set_status("Please enter name and phone.")
            return
        
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.set_status("There is a contact with this name({})".format(name))
                return
        
        try:
            new_contact = Contact(name, phone)
            self.contacts.append(new_contact)
            self.update_listbox(self.contacts)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.set_status("Contact added at the end of list.", "green")
        except ValueError as e:
            self.set_status(str(e))

    def update_contact(self):
        try:
            selection = self.listbox.curselection()
            if not selection: 
                self.set_status("Select a contact to edit.")
                return
            index = selection[0]
            self.contacts[index].name = self.name_entry.get().strip()
            self.contacts[index].phone_number = self.phone_entry.get().strip()
            self.update_listbox(self.contacts)
            self.set_status("Contact updated successfully.", "green")
        except: pass

    def search_contact(self):
        query = self.search_entry.get().lower()
        if not query:
            self.update_listbox(self.contacts)
            return
        results = [c for c in self.contacts if query in c.name.lower()]
        if not results:
            self.set_status("No results found for '{}'.".format(query))
        self.update_listbox(results)

    def delete_contact(self):
        try:
            selection = self.listbox.curselection()
            if selection:
                del self.contacts[selection[0]]
                self.update_listbox(self.contacts)
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
                self.set_status("Contact deleted.", "blue")
        except: pass

    def save_to_csv(self):
        with open(self.filename, "w") as f:
            for c in self.contacts:
                f.write(str(c.name) + "," + str(c.phone_number) + "\n")

    def load_from_csv(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            try:
                self.contacts = []
                with open(self.filename, "r") as f:
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 2:
                            self.contacts.append(Contact(parts[0], parts[1]))
            except: pass
        if not self.contacts:
            self.contacts = [Contact("Sadjad", "36029000"), Contact("Police", "110")]

    def exit_app(self):
        self.save_to_csv()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_app)
    root.mainloop()
