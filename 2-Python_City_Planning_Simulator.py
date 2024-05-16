# Task 1: File Handling for Building Records

import re

# Building class which stores the building name, number of floors, and number of offices
class Building:
    def __init__(self, name, floors, offices):
        self.name = name
        self.floors = floors
        self.offices = offices
    
    # Method to export building information to a text file
    def export_building_information(self):
        file = open("buildings.txt", "w")
        file.write(f"{self.name} - Floors: {self.floors}, Offices: {self.offices}.")
        print("The building info has been exported to the file 'buildings.txt'") # Notify user of exporting is complete
        file.close()
    
    # Method to import building information from a text file
    def import_building_information(self, pathname):
        file = open(pathname, "r")
        content = file.read()

        name = re.search(r"\b.*(?= -)", content) # Retrieve the name of the building using regex
        name = name.group()

        floors = re.search(r"(?<=Floors: )\d+", content) # Retrieve the number of floors in the building using regex
        floors = int(floors.group())

        offices = re.search(r"(?<=Offices: )\d+", content) # Retrieve the number of offices in the building using regex
        offices = int(offices.group())
        
        # Update information to match imported text file
        self.name = name
        self.floors = floors
        self.offices = offices
        print("Building info successfully imported.") # Notify user when importing is complete
    
    # Method to print all the information about a building
    def display_building_information(self):
        print(f"{self.name} has {self.floors} floors and {self.offices} offices.")

# Testing
building1 = Building("Big Skyscraper", 60, 400)
building1.display_building_information()
building1.export_building_information()

building1 = Building("Small Office", 3, 20)
building1.display_building_information()

building1.import_building_information("buildings.txt")
building1.display_building_information()