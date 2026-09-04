# this code was generated using micorosoft copilot with the following prompt:
# "create a simple beginner-friendly Python function that stores patient name, \
# practitioner name and appointment time. Explicitly prohibit a database or GUI."

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    print("Appointment booked:")
    print(f"Patient: {appointment['patient']}")
    print(f"Practitioner: {appointment['practitioner']}")
    print(f"Time: {appointment['time']}")


book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
