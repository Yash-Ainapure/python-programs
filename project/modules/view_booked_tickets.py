import tkinter as tk
import sqlite3

def view_booked_tickets_window():
    window = tk.Toplevel()
    window.title("View Booked Tickets")

    # Create a frame for the table header
    header_frame = tk.Frame(window)
    header_frame.pack(fill="x")

    # Display column headers using pack
    tk.Label(header_frame, text="Booking ID", width=15, borderwidth=1, relief="solid").pack(side="left")
    tk.Label(header_frame, text="Name", width=15, borderwidth=1, relief="solid").pack(side="left")
    tk.Label(header_frame, text="Age", width=5, borderwidth=1, relief="solid").pack(side="left")
    tk.Label(header_frame, text="Contact", width=15, borderwidth=1, relief="solid").pack(side="left")
    tk.Label(header_frame, text="Train Number", width=15, borderwidth=1, relief="solid").pack(side="left")
    tk.Label(header_frame, text="Date", width=15, borderwidth=1, relief="solid").pack(side="left")
    tk.Label(header_frame, text="Class", width=10, borderwidth=1, relief="solid").pack(side="left")

    # Fetch data from the database
    conn = sqlite3.connect('db/railway_reservation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bookings")
    records = cursor.fetchall()
    conn.close()

    # Check if records are found
    if records:
        for booking in records:
            row_frame = tk.Frame(window)
            row_frame.pack(fill="x")

            booking_id, name, age, contact, train_number, date, train_class = booking
            tk.Label(row_frame, text=booking_id, width=15, borderwidth=1, relief="solid").pack(side="left")
            tk.Label(row_frame, text=name, width=15, borderwidth=1, relief="solid").pack(side="left")
            tk.Label(row_frame, text=age, width=5, borderwidth=1, relief="solid").pack(side="left")
            tk.Label(row_frame, text=contact, width=15, borderwidth=1, relief="solid").pack(side="left")
            tk.Label(row_frame, text=train_number, width=15, borderwidth=1, relief="solid").pack(side="left")
            tk.Label(row_frame, text=date, width=15, borderwidth=1, relief="solid").pack(side="left")
            tk.Label(row_frame, text=train_class, width=10, borderwidth=1, relief="solid").pack(side="left")
    else:
        tk.Label(window, text="No bookings found", fg="red").pack()

    window.mainloop()
