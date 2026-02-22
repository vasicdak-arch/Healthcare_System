class Patient:
    def __init__(self, patient_id, name, date_of_birth, gender, contact_info):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_info = contact_info

    def __str__(self):
        return f"Patient[ID={self.patient_id}, Name={self.name}, DOB={self.date_of_birth}, Gender={self.gender}, Contact={self.contact_info}]"


class PatientManagement:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def update_patient(self, patient_id, **kwargs):
        if patient_id in self.patients:
            for key, value in kwargs.items():
                setattr(self.patients[patient_id], key, value)

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            return True
        return False

    def get_patient(self, patient_id):
        return self.patients.get(patient_id, "Patient not found")

    def input_patient(self):
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        gender = input("Enter gender: ")
        contact_info = input("Enter contact info: ")
        return Patient(patient_id, name, date_of_birth, gender, contact_info)


class Doctor:
    def __init__(self, doctor_id, name, specialty, contact_info, available_dates):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.contact_info = contact_info
        self.available_dates = available_dates

    def __str__(self):
        return f"Doctor[ID={self.doctor_id}, Name={self.name}, Specialty={self.specialty}, Contact={self.contact_info}, Available Dates={self.available_dates}]"


class DoctorManagement:
    def __init__(self):
        self.doctors = {}

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def update_doctor(self, doctor_id, **kwargs):
        if doctor_id in self.doctors:
            for key, value in kwargs.items():
                setattr(self.doctors[doctor_id], key, value)

    def delete_doctor(self, doctor_id):
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]
            return True
        return False

    def get_doctor(self, doctor_id):
        return self.doctors.get(doctor_id, "Doctor not found")

    def input_doctor(self):
        doctor_id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        specialty = input("Enter specialty: ")
        contact_info = input("Enter contact info: ")
        available_dates = input("Enter available dates (comma separated): ").split(",")
        return Doctor(doctor_id, name, specialty, contact_info, available_dates)


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date, reason):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.reason = reason

    def __str__(self):
        return f"Appointment[ID={self.appointment_id}, Patient ID={self.patient_id}, Doctor ID={self.doctor_id}, Date={self.appointment_date}, Reason={self.reason}]"


class AppointmentManagement:
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, appointment):
        self.appointments[appointment.appointment_id] = appointment

    def update_appointment(self, appointment_id, **kwargs):
        if appointment_id in self.appointments:
            for key, value in kwargs.items():
                setattr(self.appointments[appointment_id], key, value)

    def cancel_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            return True
        return False

    def get_appointment(self, appointment_id):
        return self.appointments.get(appointment_id, "Appointment not found")

    def input_appointment(self):
        appointment_id = input("Enter appointment ID: ")
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
        reason = input("Enter reason for appointment: ")
        return Appointment(appointment_id, patient_id, doctor_id, appointment_date, reason)


def main_menu():
    pm = PatientManagement()
    dm = DoctorManagement()
    am = AppointmentManagement()

    while True:
        print("\n=== Main Menu ===")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Appointments")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            manage_patients(pm)
        elif choice == "2":
            manage_doctors(dm)
        elif choice == "3":
            manage_appointments(am)
        elif choice == "4":
            break
        else:
            print("Invalid option, please try again.")


def manage_patients(pm):
    while True:
        print("\n=== Patient Management ===")
        print("1. Add Patient")
        print("2. Update Patient")
        print("3. Delete Patient")
        print("4. View Patient")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            new_patient = pm.input_patient()
            pm.add_patient(new_patient)
            print("Added Patient:", pm.get_patient(new_patient.patient_id))
        elif choice == "2":
            patient_id = input("Enter patient ID to update: ")
            if patient_id in pm.patients:
                updates = {}
                print("Leave fields empty to keep current value.")
                name = input("Enter new name: ")
                if name: updates['name'] = name
                dob = input("Enter new date of birth (YYYY-MM-DD): ")
                if dob: updates['date_of_birth'] = dob
                gender = input("Enter new gender: ")
                if gender: updates['gender'] = gender
                contact_info = input("Enter new contact info: ")
                if contact_info: updates['contact_info'] = contact_info
                pm.update_patient(patient_id, **updates)
                print("Updated Patient:", pm.get_patient(patient_id))
            else:
                print("Patient not found.")
        elif choice == "3":
            patient_id = input("Enter patient ID to delete: ")
            if pm.delete_patient(patient_id):
                print(f"Patient {patient_id} deleted successfully.")
            else:
                print("Patient not found.")
        elif choice == "4":
            patient_id = input("Enter patient ID to view: ")
            print(pm.get_patient(patient_id))
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again.")


def manage_doctors(dm):
    while True:
        print("\n=== Doctor Management ===")
        print("1. Add Doctor")
        print("2. Update Doctor")
        print("3. Delete Doctor")
        print("4. View Doctor")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            new_doctor = dm.input_doctor()
            dm.add_doctor(new_doctor)
            print("Added Doctor:", dm.get_doctor(new_doctor.doctor_id))
        elif choice == "2":
            doctor_id = input("Enter doctor ID to update: ")
            if doctor_id in dm.doctors:
                updates = {}
                print("Leave fields empty to keep current value.")
                name = input("Enter new name: ")
                if name: updates['name'] = name
                specialty = input("Enter new specialty: ")
                if specialty: updates['specialty'] = specialty
                contact_info = input("Enter new contact info: ")
                if contact_info: updates['contact_info'] = contact_info
                available_dates = input("Enter new available dates (comma separated): ")
                if available_dates: updates['available_dates'] = available_dates.split(",")
                dm.update_doctor(doctor_id, **updates)
                print("Updated Doctor:", dm.get_doctor(doctor_id))
            else:
                print("Doctor not found.")
        elif choice == "3":
            doctor_id = input("Enter doctor ID to delete: ")
            if dm.delete_doctor(doctor_id):
                print(f"Doctor {doctor_id} deleted successfully.")
            else:
                print("Doctor not found.")
        elif choice == "4":
            doctor_id = input("Enter doctor ID to view: ")
            print(dm.get_doctor(doctor_id))
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again.")


def manage_appointments(am):
    while True:
        print("\n=== Appointment Management ===")
        print("1. Schedule Appointment")
        print("2. Update Appointment")
        print("3. Cancel Appointment")
        print("4. View Appointment")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            new_appointment = am.input_appointment()
            am.schedule_appointment(new_appointment)
            print("Scheduled Appointment:", am.get_appointment(new_appointment.appointment_id))
        elif choice == "2":
            appointment_id = input("Enter appointment ID to update: ")
            if appointment_id in am.appointments:
                updates = {}
                print("Leave fields empty to keep current value.")
                patient_id = input("Enter new patient ID: ")
                if patient_id: updates['patient_id'] = patient_id
                doctor_id = input("Enter new doctor ID: ")
                if doctor_id: updates['doctor_id'] = doctor_id
                appointment_date = input("Enter new appointment date (YYYY-MM-DD): ")
                if appointment_date: updates['appointment_date'] = appointment_date
                reason = input("Enter new reason for appointment: ")
                if reason: updates['reason'] = reason
                am.update_appointment(appointment_id, **updates)
                print("Updated Appointment:", am.get_appointment(appointment_id))
            else:
                print("Appointment not found.")
        elif choice == "3":
            appointment_id = input("Enter appointment ID to cancel: ")
            if am.cancel_appointment(appointment_id):
                print(f"Appointment {appointment_id} canceled successfully.")
            else:
                print("Appointment not found.")
        elif choice == "4":
            appointment_id = input("Enter appointment ID to view: ")
            print(am.get_appointment(appointment_id))
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main_menu()
