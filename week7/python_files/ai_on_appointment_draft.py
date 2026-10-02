from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"


class InvalidStatusTransitionError(Exception):
    """Raised when an appointment lifecycle transition is invalid."""


class Appointment:
    def __init__(
        self,
        appointment_id,
        patient,
        practitioner,
        date_time: datetime,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED,
    ):
        if patient is None:
            raise ValueError("patient is required")

        if practitioner is None:
            raise ValueError("practitioner is required")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def cancel(self):
        """Cancel a scheduled appointment without deleting it."""
        if self.status != AppointmentStatus.SCHEDULED:
            raise InvalidStatusTransitionError(
                "Only scheduled appointments can be cancelled."
            )

        self.status = AppointmentStatus.CANCELLED

    def reschedule(self, new_date_time: datetime):
        """Change the appointment time while it is still scheduled."""
        if self.status != AppointmentStatus.SCHEDULED:
            raise InvalidStatusTransitionError(
                "Only scheduled appointments can be rescheduled."
            )

        self.date_time = new_date_time
