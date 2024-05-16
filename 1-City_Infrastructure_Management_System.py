# Task 1: Vehicle Registration System

# Vehicle class which store registration number, type of car, and owner
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    # Method to change owner of a vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner

    # Prints all vehicle information
    def display_vehicle_details(self):
        print(f"{self.type} owned by {self.owner}. Registration: {self.reg_num}")

# Testing
vehicle1 = Vehicle(101, "Toyota", "Bob")
vehicle2 = Vehicle(102, "Mercedes", "Dante")
vehicle3 = Vehicle(103, "BMW", "Ron")

vehicle2.display_vehicle_details()
vehicle3.display_vehicle_details()

print("Original owner of vehicle 1: ", end="")
vehicle1.display_vehicle_details()

vehicle1.update_owner("Godzilla")
print("New owner of vehicle 1: ", end="")
vehicle1.display_vehicle_details()
print()

# Task 2: Event Management System Enhancement

# Event class which stores its name, date, and participants which starts at 0 when initialized
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0
    
    # Method to add any number of participant to the event
    def add_participant(self, num_of_participants):
        self.participants += num_of_participants
    
    # Method which returns total number of participants added
    def get_participant_count(self):
        return self.participants
    
    # Prints all event information
    def get_party_information(self):
        print(f"{self.name} will take place on {self.date}. There are currently {self.participants} guests.")
    
# Testing
halloween_party = Event("Halloween Party", "10-31-2024")
halloween_party.add_participant(20)
halloween_party.get_party_information()
halloween_party.add_participant(7)
print(f"There are currently {halloween_party.get_participant_count()} participants attending.")