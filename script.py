import mysql.connector
from mysql.connector import Error
import time

HOST = "localhost"
USER = "root"
PASS = "farwa"
DB = "hospital"  

class PatientManagement:
    def __init__(self):
        self.total_execution_time = 0.0
        self.conn = None
        try:
            self.conn = mysql.connector.connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DB
            )
            if self.conn.is_connected():
                print("Database connection successful!")
        except Error as e:
            print(f"Database connection failed: {e}")
            exit(1)

    def __del__(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()

    def increment_time_complexity(self, time_taken):
        self.total_execution_time += time_taken

    def display_time_complexity(self):
        print(f"Total execution time: {self.total_execution_time} seconds.")

    def add_patient(self, patient_id, first_name, last_name, age, gender, blood_group, contact, cnic, address):
        start_time = time.time()
        query = ("INSERT INTO patients (patient_id, first_name, last_name, age, gender, blood_group, contact, cnic, address) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (patient_id, first_name, last_name, age, gender, blood_group, contact, cnic, address)
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, values)
            self.conn.commit()
            print("Patient added successfully.")
        except Error as e:
            print(f"Failed to add patient: {e}")
        cursor.close()
        end_time = time.time()
        self.increment_time_complexity(end_time - start_time)

    def display_patients(self):
        start_time = time.time()
        query = "SELECT * FROM patients"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            print("Patients in the system:")
            for row in rows:
                print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Age: {row[3]}, Gender: {row[4]}, Blood Group: {row[5]}, Contact: {row[6]}, CNIC: {row[7]}, Address: {row[8]}")
        except Error as e:
            print(f"Failed to retrieve patients: {e}")
        cursor.close()
        end_time = time.time()
        self.increment_time_complexity(end_time - start_time)

    def search_patient_by_name(self, first_name):
        start_time = time.time()
        query = "SELECT * FROM patients WHERE first_name = %s"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, (first_name,))
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Patient found - ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Age: {row[3]}, Gender: {row[4]}, Blood Group: {row[5]}, Contact: {row[6]}, CNIC: {row[7]}, Address: {row[8]}")
            else:
                print("Patient not found.")
        except Error as e:
            print(f"Failed to search patient: {e}")
        cursor.close()
        end_time = time.time()
        self.increment_time_complexity(end_time - start_time)

    def search_patient_by_id(self, patient_id):
        start_time = time.time()
        query = "SELECT * FROM patients WHERE patient_id = %s"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, (patient_id,))
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Patient found - ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Age: {row[3]}, Gender: {row[4]}, Blood Group: {row[5]}, Contact: {row[6]}, CNIC: {row[7]}, Address: {row[8]}")
            else:
                print("Patient not found.")
        except Error as e:
            print(f"Failed to search patient: {e}")
        cursor.close()
        end_time = time.time()
        self.increment_time_complexity(end_time - start_time)

    def remove_patient(self, patient_id):
        start_time = time.time()
        query = "DELETE FROM patients WHERE patient_id = %s"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, (patient_id,))
            self.conn.commit()
            print("Patient removed successfully.")
        except Error as e:
            print(f"Failed to remove patient: {e}")
        cursor.close()
        end_time = time.time()
        self.increment_time_complexity(end_time - start_time)


def main():
    pm = PatientManagement()
    while True:
        print("\nPatient Management System Menu:")
        print("1. Add Patient")
        print("2. Display All Patients")
        print("3. Search Patient by Name")
        print("4. Search Patient by ID")
        print("5. Remove Patient")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            patient_id = input("Enter Patient ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            blood_group = input("Enter Blood Group: ")
            contact = input("Enter Contact: ")
            cnic = input("Enter CNIC: ")
            address = input("Enter Address: ")
            pm.add_patient(patient_id, first_name, last_name, age, gender, blood_group, contact, cnic, address)
        elif choice == 2:
            pm.display_patients()
        elif choice == 3:
            first_name = input("Enter First Name to search: ")
            pm.search_patient_by_name(first_name)
        elif choice == 4:
            patient_id = input("Enter Patient ID to search: ")
            pm.search_patient_by_id(patient_id)
        elif choice == 5:
            patient_id = input("Enter Patient ID to remove: ")
            pm.remove_patient(patient_id)
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    pm.display_time_complexity()

if __name__ == "__main__":
    main()
