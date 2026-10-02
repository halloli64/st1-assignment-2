from smartcare_v04 import Patient, Practitioner, Appointment


def check(description, condition):
    if condition:
        print("PASS:", description)
    else:
        print("FAIL:", description)


print("--- Creating objects and using accessors ---")
patient = Patient(1, "Alex Taylor", "2002-05-14",
                  {"phone": "0400000000", "email": "alex@example.com"})
practitioner = Practitioner(10, "Dr Morgan",
                            {"phone": "0299999999"})
appointment = Appointment(100, patient, practitioner, "2026-10-10 10:30")

check("Patient ID accessor", patient.get_patient_id() == 1)
check("Patient name accessor", patient.get_name() == "Alex Taylor")
check("Patient starts active", patient.get_is_active() is True)
check("Practitioner name accessor", practitioner.get_name() == "Dr Morgan")
check("Appointment starts scheduled", appointment.get_status() == "SCHEDULED")
check("Appointment refers to the supplied patient", appointment.get_patient() is patient)

print("\n--- Updating details ---")
patient.update_details("Alex T", "2002-05-14",
                       {"phone": "0411111111"})
check("Patient details updated", patient.get_name() == "Alex T")
check("Updated contact details stored",
      patient.get_contact_details()["phone"] == "0411111111")

practitioner.update_details("Dr Morgan-Smith", {"phone": "0288888888"})
check("Practitioner details updated",
      practitioner.get_name() == "Dr Morgan-Smith")

print("\n--- Validation checks ---")
try:
    Patient(0, "Invalid ID", "2000-01-01", {})
    check("Rejects a non-positive patient ID", False)
except ValueError:
    check("Rejects a non-positive patient ID", True)

try:
    Patient(2, "   ", "2000-01-01", {})
    check("Rejects a blank patient name", False)
except ValueError:
    check("Rejects a blank patient name", True)

try:
    Patient(3, "Casey", "2000-01-01", [])
    check("Rejects contact details that are not a dictionary", False)
except ValueError:
    check("Rejects contact details that are not a dictionary", True)

print("\n--- Appointment lifecycle ---")
check("First cancellation succeeds", appointment.cancel() is True)
check("Status becomes cancelled", appointment.get_status() == "CANCELLED")
check("Second cancellation is rejected", appointment.cancel() is False)
check("Cannot reschedule a cancelled appointment",
      appointment.reschedule("2026-10-11 11:00") is False)

another_appointment = Appointment(101, patient, practitioner,
                                  "2026-10-12 09:00")
check("Can reschedule a scheduled appointment",
      another_appointment.reschedule("2026-10-13 09:30") is True)
check("New appointment time is stored",
      another_appointment.get_date_time() == "2026-10-13 09:30")

print("\n--- Deactivation ---")
patient.deactivate()
check("Patient becomes inactive", patient.get_is_active() is False)

print("\nManual checks complete.")
