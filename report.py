import sqlite3

def generate_report():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    print("\n====== Attendance Report ======")

    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No attendance records found.")
    else:
        print("{:<5} {:<20} {:<15} {:<10}".format("ID", "Name", "Date", "Status"))
        print("-" * 55)

        for row in records:
            print("{:<5} {:<20} {:<15} {:<10}".format(row[0], row[1], row[2], row[3]))

    conn.close()

if __name__ == "__main__":
    generate_report()
