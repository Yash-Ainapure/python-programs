import tkinter as tk
from tkinter import messagebox
import sqlite3

def cancel_ticket_window():
    def cancel_ticket():
        booking_id = entry_booking_id.get()

        if booking_id:
            conn = sqlite3.connect('db/railway_reservation.db')
            cursor = conn.cursor()
            rows_deleted = cursor.execute("DELETE FROM Bookings WHERE booking_id = ?", (booking_id,)).rowcount
            conn.commit()
            conn.close()
            if rows_deleted > 0:
                messagebox.showinfo("Success", "Booking canceled successfully!")
            else:
                messagebox.showerror("Error", "Booking ID not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter the Booking ID.")

    window = tk.Toplevel()
    window.title("Cancel Booking")

    tk.Label(window, text="Booking ID").grid(row=0, column=0)
    entry_booking_id = tk.Entry(window)
    entry_booking_id.grid(row=0, column=1)

    tk.Button(window, text="Cancel Booking", command=cancel_ticket).grid(row=1, columnspan=2)

    window.mainloop()
