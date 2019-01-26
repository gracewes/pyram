import json 

class person:

    # class definition for a person using the platform
    
    def __init__(self, location, radius, interest, contact_info='' ):
        self.location = location 
        self.radius = radius
        self.interest = interest
        self.contact_info = contact_info

    def get_location(self):
        return self.location 

    def get_radius(self):
        return self.radius 

    def get_interest(self):
        return self.interest
    
    def get_contact_info(self):
        # might want to check if contact info has been inputed yet
        return self.contact_info

    def change_location(self, new_location):
        self.location = new_location

    def change_radius(self, new_radius):
        self.radius = new_radius
    
    def change_interest(self, new_interest):
        self.interest = new_interest

    def change_contact_info(self, new_contact_info):
        # can be used to add new contact info since the default for contact info is an empty string 
        self.contact_info = new_contact_info

    def make_json_person(self):
        person_data = {}

        person_data['location'] = self.location
        person_data['radius'] = self.radius
        person_data['interest'] = self.interest
        person_data['contact info']= self.contact_info

        json_person = json.dumps(person_data)

        return json_person




    
        