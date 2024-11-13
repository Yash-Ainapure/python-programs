import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db/railway_reservation.db')
cursor = conn.cursor()

# Create Trains table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Trains (
    train_number INTEGER PRIMARY KEY,
    train_name TEXT,
    route TEXT,
    timing TEXT,
    price REAL
)
''')

# Create Bookings table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    contact TEXT,
    train_number INTEGER,
    date TEXT,
    class TEXT,
    FOREIGN KEY (train_number) REFERENCES Trains(train_number)
)
''')

# Insert initial train data
cursor.execute('''
INSERT INTO Trains (train_number, train_name, route, timing, price)
VALUES
    (101, 'Express A', 'City X - City Y', '09:00 - 12:00', 100.0),
    (102, 'Express B', 'City Y - City Z', '13:00 - 16:00', 120.0)
''')

conn.commit()
conn.close()

print("Database setup complete.")
