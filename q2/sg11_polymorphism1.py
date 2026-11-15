# I would like to note that I do not recall an initial Hospoital 1ST
# Billing System Code (FA 2 under sg 10- method overriding) 2ND
# given to us, so this is rather a new code for sg 11, not an enhanced one 3RD


class Patient: #the blueprnt for the patient class, which is the parent class of the other two classes
    def __init__(self, name, bill_amount): 
        self.__name = name
        self.__bill_amount = bill_amount

# the init function initializes the attrbutes self.__name and self.__bill_amount when a Patient object is created. 
# double underscore was used snce this is confidential data, and it must be kept private information, also shows encapsulation
# self.__name stores the name of the patient, and cannot be changed directly from the ooutside class
# self.__bill_amount stores the patient's original hospital amount, which is also kept private 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

# getters and setter are used here since both __name and __bill amoount are private 1ST
# with these methods, the values of the attributes can be accessed and modified safely
# get retieves and returns the value
# set updates or changes the value


    def display_patient_type(self):
        print("Patient Type: Regular Patient")

# calculate_bill returns the original bill vaue wth no diiscounts applied
# displa_patient_type prints out that the patient is a regular patient

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8  # 20% discount for senior patients, since 20/100 = 0.2, and 1 - 0.2 = 0.8
    # through (Patient), the SeniorPatient suubclass inherits everything from the Patient class, 1ST
# this includes the attributes and methods, but the calculate_bill method is overridden using the same method name, but with a different implementation 2ND
# to apply a 20% discount for senior patients 3RD

    def display_patient_type(self):
        print("Patient Type: Senior Patient")

# this overrides the display_patient_type method from the Patient class to indicate that the patient is a senior patient 

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85  # 15% discount for patients that are PhilHealth members, since 15/100 = 0.15, and 1 - 0.15 = 0.85
# through (Patient), the PhilHealthPatient subclass inherits everything from the Patient class, 1ST
# the calculate_bill method is overridden using the same method name, but with a different implementation as well 2ND
# but this time, it applies a 15% discount for patients that are PhilHealth members 3RD

    def display_patient_type(self):
        print("Patient Type: Philhealth Member")
#this overrides the display_patient_type method from the Patient class to indicate that the patient is a PhilHealth member

print("Hospital Billing System")
print("------------------------")

p1 = Patient("John Doe", 15000.0)
print(f"Patient Name: {p1.get_name()}")
p1.display_patient_type()
print(f"Original Bill Amount: ₱{p1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p1.calculate_bill():,.2f}")
# p1.get_name() retrieves the name of the patient
# p1.display_patient_type() displays the type of patient
# p1.get_bill_amount() retrieves the original bill amount, and p1.calculate_bill() calculates the final bill amount (which is the same as the original bill amount for regular patients)

p2 = SeniorPatient("Maria Santos", 15000.0)
print(f"\nPatient Name: {p2.get_name()}")
p2.display_patient_type()
print(f"Original Bill Amount: ₱{p2.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p2.calculate_bill():,.2f}")
# p2.get_name() retrieves the name of the patient
# p2.display_patient_type() displays the type of patient
# p2.get_bill_amount() retrieves the original bill amount
# p2.calculate_bill() calculates the final bill amount (which is 20% less than the original bill)

p3 = PhilHealthPatient("Pedro Reyes", 15000.0)
print(f"\nPatient Name: {p3.get_name()}")
p3.display_patient_type()
print(f"Original Bill Amount: ₱{p3.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p3.calculate_bill():,.2f}")
# p3.get_name() retrieves the name of the patient
# p3.display_patient_type() displays the type of patient
# p3.get_bill_amount() retrieves the original bill amount
# p3.calculate_bill() calculates the final bill amount (which is 15% less than the original bill)

# :,.2f is used to format the numbers to have commas and two decmal places
# i would like to also acknowledge that I used google for the Peso sign symbol copy 1ST
# and also for the comma thingy since my original code did not have commas in the peso values 2ND
