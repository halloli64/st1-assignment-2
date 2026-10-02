class Patient:
    def __init__(self, patient_id, name, date_of_birth, contact_details):
        if not name or not name.strip():
            raise ValueError("Patient name cannot be blank")

        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_details = contact_details
        self.is_active = True

    def deactivate(self):
        self.is_active = False