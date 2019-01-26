import json 
from person import person

class database:
    '''makes a json file of people sorted by interests '''
    def __init__(self):
        self.interests = {}
        self.database = {"interests" : self.interests }
    
    def add_interest(self, new_interest, person_list):
        
        if new_interest in self.interests:
            print(new_interest, ' already in interests dictionary')
        else:

            # create a new dictionary and store empty list of people 
            interest = dict(people= person_list)

            #add new interest to interests dict
            self.interests[new_interest] = interest
        
    def get_interest(self, person):
        '''given a person object thats been converted to dict, returns the interest'''
       
        return person['interest']

    def add_person(self, person_dict):
        '''adds person to database
           takes in person dictionaries, not json or person object'''

        person_interest = self.get_interest(person_dict)

        if person_interest in self.interests:
            #if interest already exists, simply add new person to person list
            self.interests[person_interest]['people'].append(person_dict)
        else:
            #if interest doesnt exits yet, create new interest, addd person to person list
            self.add_interest(person_interest, [])
            self.interests[person_interest]['people'].append(person_dict)

    def add_person_json_file(self, file_name):
        '''adds person to database from json file'''
        with open(file_name) as json_file:
            person_dict = json.load(json_file)
        
        self.add_person(person_dict)

    def add_person_obj(self, person_obj):
        '''adds person to database from person object'''

        person_dict = person_obj.person_data_dict()
        self.add_person(person_dict)
    

    def export_json(self):
        json_database = json.dumps(self.database)
        return json_database

        
