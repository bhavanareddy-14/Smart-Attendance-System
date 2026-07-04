import sqlite3

def view_attendance():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()

    print("\n===== Attendance Records =====")
    if not records:
        print("No attendance records found.")
    else:
        for record in records:
            print(f"ID: {record[0]}")
            print(f"Student: {record[1]}")
            print(f"Date: {record[2]}")
            print(f"Status: {record[3]}")
            print("-" * 30)

    conn.close()

if __name__ == "__main__":
    view_attendance()
