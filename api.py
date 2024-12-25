from datetime import datetime
class AppointmentSystem:
    def __init__(self):
        self.users = {}
        self.avail = {}
        self.bookings = {}

    def aut(self, user_type, user_id):
        if user_id not in self.users:
            self.users[user_id] = user_type
        print(f"{user_type} {user_id} authenticated successfully.")

    def set_avail(self, professor_id, available_slots):
        if self.users.get(professor_id) != "Professor":
            print("Error: Only professors can set availability.")
            return
        self.avail[professor_id] = available_slots
        print(f"Professor {professor_id} set availability: {available_slots}")

    def view_avail(self, professor_id):
        return self.avail.get(professor_id, [])

    def book_app(self, student_id, professor_id, time_slot):
        if self.users.get(student_id) != "Student":
            print("Error: Only students can book appointments.")
            return

        if professor_id not in self.avail or time_slot not in self.avail[professor_id]:
            print("Error: Selected time slot is not available.")
            return

        self.bookings.setdefault(professor_id, {})[time_slot] = student_id
        self.avail[professor_id].remove(time_slot)
        print(f"Student {student_id} booked appointment with Professor {professor_id} at {time_slot}.")

    def cancel_app(self, professor_id, time_slot):
        if self.users.get(professor_id) != "Professor":
            print("Error: Only professors can cancel appointments.")
            return

        if professor_id in self.bookings and time_slot in self.bookings[professor_id]:
            student_id = self.bookings[professor_id].pop(time_slot)
            self.avail[professor_id].append(time_slot)
            print(f"Professor {professor_id} canceled appointment with Student {student_id} at {time_slot}.")
        else:
            print("Error: No appointment exists for the given time slot.")

    def check_apps(self, student_id):
        appointments = [
            (professor_id, time_slot)
            for professor_id, slots in self.bookings.items()
            for time_slot, booked_student in slots.items()
            if booked_student == student_id
        ]
        return appointments
sys = AppointmentSystem()
sys.aut("Student", "A1")
sys.aut("Professor", "P1")
sys.set_avail("P1", ["T1", "T2", "T3"])
print("Available slots for P1:", sys.view_avail("P1"))
sys.book_app("A1", "P1", "T1")
sys.aut("Student", "A2")
print("Now Available slots for P1:", sys.view_avail("P1"))
sys.book_app("A2", "P1", "T2")
sys.cancel_app("P1", "T1")
print("Appointments for A1:", sys.check_apps("A1"))
