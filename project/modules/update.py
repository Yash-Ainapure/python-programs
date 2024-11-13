import tkinter as tk
from tkinter import messagebox
import sqlite3

def update_ticket_window():
    def search_ticket():
        booking_id = entry_booking_id.get()
        conn = sqlite3.connect('db/railway_reservation.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bookings WHERE booking_id = ?", (booking_id,))
        record = cursor.fetchone()
        conn.close()

        if record:
            entry_name.insert(0, record[1])
            entry_age.insert(0, record[2])
            entry_contact.insert(0, record[3])
            entry_train.insert(0, record[4])
            entry_date.insert(0, record[5])
            entry_class.insert(0, record[6])
        else:
            messagebox.showwarning("Not Found", "Booking ID not found.")

    def update_ticket():
        booking_id = entry_booking_id.get()
        name = entry_name.get()
        age = entry_age.get()
        contact = entry_contact.get()
        train_number = entry_train.get()
        date = entry_date.get()
        train_class = entry_class.get()

        if booking_id and name and age and contact and train_number and date and train_class:
            conn = sqlite3.connect('db/railway_reservation.db')
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Bookings
                SET name = ?, age = ?, contact = ?, train_number = ?, date = ?, class = ?
                WHERE booking_id = ?
            """, (name, int(age), contact, int(train_number), date, train_class, int(booking_id)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Booking updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    window = tk.Toplevel()
    window.title("Update Booking")

    tk.Label(window, text="Booking ID").grid(row=0, column=0)
    entry_booking_id = tk.Entry(window)
    entry_booking_id.grid(row=0, column=1)
    tk.Button(window, text="Search", command=search_ticket).grid(row=0, column=2)

    tk.Label(window, text="Name").grid(row=1, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=1, column=1)

    tk.Label(window, text="Age").grid(row=2, column=0)
    entry_age = tk.Entry(window)
    entry_age.grid(row=2, column=1)

    tk.Label(window, text="Contact").grid(row=3, column=0)
    entry_contact = tk.Entry(window)
    entry_contact.grid(row=3, column=1)

    tk.Label(window, text="Train Number").grid(row=4, column=0)
    entry_train = tk.Entry(window)
    entry_train.grid(row=4, column=1)

    tk.Label(window, text="Date (YYYY-MM-DD)").grid(row=5, column=0)
    entry_date = tk.Entry(window)
    entry_date.grid(row=5, column=1)

    tk.Label(window, text="Class (e.g., AC, Sleeper)").grid(row=6, column=0)
    entry_class = tk.Entry(window)
    entry_class.grid(row=6, column=1)

    tk.Button(window, text="Update Booking", command=update_ticket).grid(row=7, columnspan=2)

    window.mainloop()
