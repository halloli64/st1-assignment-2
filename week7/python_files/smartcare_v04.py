class Patient:
    def __init__(self, patient_id, name, date_of_birth, contact_details):
        if not isinstance(patient_id, int) or isinstance(patient_id, bool) or patient_id <= 0:
            raise ValueError("Patient ID must be a positive integer.")
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Patient name cannot be empty.")
        if not isinstance(contact_details, dict):
            raise ValueError("Contact details must be stored in a dictionary.")

        self.__patient_id = patient_id
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__contact_details = contact_details
        self.__is_active = True

    # Accessor methods
    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_contact_details(self):
        return self.__contact_details

    def get_is_active(self):
        return self.__is_active

    # Mutator method
    def update_details(self, name, date_of_birth, contact_details):
        # Validate all supplied values before changing any stored details.
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Patient name cannot be empty.")
        if not isinstance(contact_details, dict):
            raise ValueError("Contact details must be stored in a dictionary.")

        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__contact_details = contact_details

    def deactivate(self):
        self.__is_active = False


class Practitioner:
    def __init__(self, practitioner_id, name, contact_details):
        if not isinstance(practitioner_id, int) or isinstance(practitioner_id, bool) or practitioner_id <= 0:
            raise ValueError("Practitioner ID must be a positive integer.")
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Practitioner name cannot be empty.")
        if not isinstance(contact_details, dict):
            raise ValueError("Contact details must be stored in a dictionary.")

        self.__practitioner_id = practitioner_id
        self.__name = name
        self.__contact_details = contact_details

    # Accessor methods
    def get_practitioner_id(self):
        return self.__practitioner_id

    def get_name(self):
        return self.__name

    def get_contact_details(self):
        return self.__contact_details

    # Mutator method
    def update_details(self, name, contact_details):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Practitioner name cannot be empty.")
        if not isinstance(contact_details, dict):
            raise ValueError("Contact details must be stored in a dictionary.")

        self.__name = name
        self.__contact_details = contact_details


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time):
        if not isinstance(appointment_id, int) or isinstance(appointment_id, bool) or appointment_id <= 0:
            raise ValueError("Appointment ID must be a positive integer.")
        if not isinstance(patient, Patient):
            raise ValueError("Appointment patient must be a Patient object.")
        if not isinstance(practitioner, Practitioner):
            raise ValueError("Appointment practitioner must be a Practitioner object.")

        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__practitioner = practitioner
        self.__date_time = date_time
        self.__status = "SCHEDULED"

    # Accessor methods
    def get_appointment_id(self):
        return self.__appointment_id

    def get_patient(self):
        return self.__patient

    def get_practitioner(self):
        return self.__practitioner

    def get_date_time(self):
        return self.__date_time

    def get_status(self):
        return self.__status

    # Appointment actions
    def cancel(self):
        if self.__status == "SCHEDULED":
            self.__status = "CANCELLED"
            return True
        return False

    def reschedule(self, new_date_time):
        if self.__status == "SCHEDULED":
            self.__date_time = new_date_time
            return True
        return False
