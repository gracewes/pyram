import json 

class person:

    # class definition for a person using the platform
    
    def __init__(self, user_name, email, location, radius, interest, contact_info='None' ):
        # construct person
        self.user_name = user_name
        self.email = email
        self.location = location 
        self.radius = radius
        self.interest = interest
        self.contact_info = contact_info

    def get_user_name(self):
        return self.user_name

    def get_email(self):
        return self.user_name
    
    def get_location(self):
        return self.location 

    def get_radius(self):
        return self.radius 

    def get_interest(self):
        return self.interest
    
    def get_contact_info(self):
        # might want to check if contact info has been inputed yet
        return self.contact_info

    def change_user_name(self, new_user_name):
        self.user_name = new_user_name

    def change_email(self, new_email):
        self.email = new_email

    def change_location(self, new_location):
        self.location = new_location

    def change_radius(self, new_radius):
        self.radius = new_radius
    
    def change_interest(self, new_interest):
        self.interest = new_interest

    def change_contact_info(self, new_contact_info):
        # can be used to add new contact info since the default for contact info is an empty string 
        self.contact_info = new_contact_info

    def person_data_dict(self):
        person_data = {}

        person_data['name'] = self.user_name
        person_data['email'] = self.email
        person_data['location'] = self.location
        person_data['radius'] = self.radius
        person_data['interest'] = self.interest
        person_data['contact info']= self.contact_info

        return person_data

    def make_json_person(self):
        # exports person's data as json object 
        json_person = json.dumps(self.person_data_dict())

        return json_person




    
        