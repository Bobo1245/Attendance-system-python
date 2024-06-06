
class AttendanceSystem:
    def __init__(self, filename):
        self.filename = filename
        self.attendance = self.load_attendance()

    def load_attendance(self):
        try:
            with open(self.filename, 'r') as file:
                attendance = {}
                for line in file:
                    name, status = line.strip().split(',')
                    attendance[name] = status == 'True'
                return attendance
        except FileNotFoundError:
            return {}

    def save_attendance(self):
        with open(self.filename, 'w') as file:
            for name, status in self.attendance.items():
                file.write(f"{name},{status}\n")

    def mark_attendance(self, name):
        self.attendance[name] = True
        self.save_attendance()

    def mark_absence(self, name):
        self.attendance[name] = False
        self.save_attendance()

    def check_attendance(self, name):
        return self.attendance.get(name, False)


attendance_system = AttendanceSystem('attendance.txt')

while True:
    print("1. Mark Attendance")
    print("2. Mark Absence")
    print("3. Check Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        attendance_system.mark_attendance(name)
    elif choice == '2':
        name = input("Enter name: ")
        attendance_system.mark_absence(name)
    elif choice == '3':
        name = input("Enter name: ")
        attendance = attendance_system.check_attendance(name)
        print(f"Attendance: {attendance}")
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
