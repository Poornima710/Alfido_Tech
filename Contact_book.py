import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Labels
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)

        # Entries
        self.name_entry = tk.Entry(root, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_entry = tk.Entry(root, textvariable=self.phone_var)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_entry = tk.Entry(root, textvariable=self.address_var)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(root, text="View Contact List", command=self.view_contact_list).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        name = self.name_var.get()
        phone_number = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone_number:
            contact = Contact(name, phone_number, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    def view_contact_list(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact.name}: {contact.phone_number}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts found!")

    def search_contact(self):
        search_term = self.name_var.get()
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
            if found_contacts:
                contact_list = "\n".join([f"{contact.name}: {contact.phone_number}" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No contacts found!")
        else:
            messagebox.showerror("Error", "Please enter a search term!")

    def update_contact(self):
        name = self.name_var.get()
        phone_number = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone_number:
            for contact in self.contacts:
                if contact.name == name:
                    contact.phone_number = phone_number
                    contact.email = email
                    contact.address = address
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    break
            else:
                messagebox.showerror("Error", "Contact not found!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    def delete_contact(self):
        name = self.name_var.get()

        if name:
            for contact in self.contacts:
                if contact.name == name:
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    break
            else:
                messagebox.showerror("Error", "Contact not found!")
        else:
            messagebox.showerror("Error", "Please enter the name of the contact to delete!")
1
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
