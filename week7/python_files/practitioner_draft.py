class Practitioner:
    def __init__(self, practitioner_id, name, contact_details):
        if not name or not name.strip():
            raise ValueError("Practitioner name cannot be blank")

        self.practitioner_id = practitioner_id
        self.name = name
        self.contact_details = contact_details
