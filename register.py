import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT UNIQUE
)
""")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

cursor.execute(
    "INSERT INTO students(name, roll_no) VALUES(?, ?)",
    (name, roll_no)
)

conn.commit()
print("Student Registered Successfully!")
conn.close()
