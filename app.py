import sqlite3

# Connect to database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

print("====== Smart Attendance System ======")

name = input("Enter Student Name: ")
date = input("Enter Date (DD-MM-YYYY): ")
status = input("Enter Attendance (Present/Absent): ")

cursor.execute(
    "INSERT INTO attendance (student_name, date, status) VALUES (?, ?, ?)",
    (name, date, status)
)

conn.commit()

print("\nAttendance Recorded Successfully!")
print(f"Student: {name}")
print(f"Date: {date}")
print(f"Status: {status}")

conn.close()
