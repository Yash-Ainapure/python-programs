import tkinter as tk
from tkinter import ttk, messagebox
from modules.booking import book_ticket_window
from modules.update import update_ticket_window
from modules.cancel import cancel_ticket_window
from modules.view_trains import view_trains_window
from modules.view_booked_tickets import view_booked_tickets_window

def main():
    root = tk.Tk()
    root.title("Railway Reservation System")
    root.geometry("400x400")

    # Buttons to navigate to different functionalities
    ttk.Button(root, text="Book Ticket", command=book_ticket_window).pack(pady=10)
    ttk.Button(root, text="Update Booking", command=update_ticket_window).pack(pady=10)
    ttk.Button(root, text="Cancel Booking", command=cancel_ticket_window).pack(pady=10)
    ttk.Button(root, text="View Train Timings", command=view_trains_window).pack(pady=10)
    ttk.Button(root, text="View Booked Tickets", command=view_booked_tickets_window).pack(pady=10)


    root.mainloop()

if __name__ == "__main__":  
    main()
