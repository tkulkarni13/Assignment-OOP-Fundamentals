# Task 1: Public Transportation Module

class Bus:
    # class variables which stay constant for all buses in the system
    city_name = "New York"
    base_fare = "$2.50"

    def __init__(self, route_number, passenger_capacity):
        # Instance variable which vary from bus to bus
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity
    
    # Method to display all information about the bus
    def display_bus_information(self):
        print(f"Bus {self.route_number}: City: {self.city_name}, Base Fare: {self.base_fare}, Passenger Capacity: {self.passenger_capacity}")

# Testing
bus1 = Bus(5162, 30)
bus2 = Bus(1366, 50)

# Route number and passenger capacity may change from bus to bus, but the city and base fare don't change (instance vs class variables)
bus1.display_bus_information()
bus2.display_bus_information()