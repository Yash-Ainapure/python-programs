import tkinter as tk
import sqlite3

def view_trains_window():
    window = tk.Toplevel()
    window.title("View Train Timings")

    conn = sqlite3.connect('db/railway_reservation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Trains")
    records = cursor.fetchall()
    conn.close()

    tk.Label(window, text="Train Details").grid(row=0, column=0, columnspan=4)

    for idx, train in enumerate(records, start=1):
        train_number, train_name, route, timing, price = train
        tk.Label(window, text=f"{train_number} - {train_name}").grid(row=idx, column=0)
        tk.Label(window, text=f"Route: {route}").grid(row=idx, column=1)
        tk.Label(window, text=f"Timing: {timing}").grid(row=idx, column=2)
        tk.Label(window, text=f"Price: ${price}").grid(row=idx, column=3)

    window.mainloop()
