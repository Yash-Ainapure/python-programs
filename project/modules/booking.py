import tkinter as tk
from tkinter import messagebox
import sqlite3

def book_ticket_window():
    def book_ticket():
        name = entry_name.get()
        age = entry_age.get()
        contact = entry_contact.get()
        train_number = entry_train.get()
        date = entry_date.get()
        train_class = entry_class.get()

        if name and age and contact and train_number and date and train_class:
            conn = sqlite3.connect('db/railway_reservation.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Bookings (name, age, contact, train_number, date, class) VALUES (?, ?, ?, ?, ?, ?)",
                           (name, int(age), contact, int(train_number), date, train_class))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Ticket booked successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    # Create window
    window = tk.Toplevel()
    window.title("Book Ticket")

    # Widgets for booking form
    tk.Label(window, text="Name").grid(row=0, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1)

    tk.Label(window, text="Age").grid(row=1, column=0)
    entry_age = tk.Entry(window)
    entry_age.grid(row=1, column=1)

    tk.Label(window, text="Contact").grid(row=2, column=0)
    entry_contact = tk.Entry(window)
    entry_contact.grid(row=2, column=1)

    tk.Label(window, text="Train Number").grid(row=3, column=0)
    entry_train = tk.Entry(window)
    entry_train.grid(row=3, column=1)

    tk.Label(window, text="Date (YYYY-MM-DD)").grid(row=4, column=0)
    entry_date = tk.Entry(window)
    entry_date.grid(row=4, column=1)

    tk.Label(window, text="Class (e.g., AC, Sleeper)").grid(row=5, column=0)
    entry_class = tk.Entry(window)
    entry_class.grid(row=5, column=1)

    tk.Button(window, text="Book Ticket", command=book_ticket).grid(row=6, columnspan=2)

    window.mainloop()
