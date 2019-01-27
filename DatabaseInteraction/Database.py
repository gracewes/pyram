import json

class Database:
    '''makes a json file of people sorted by interests '''
    def __init__(self):
        self.interests = {}
        self.database = {"interests" : self.interests }
    
    def get_json(self, filename):
        '''get a database from a json file'''
        try:
            with open(filename) as json_file:
                self.database = json.load(json_file)

        except IOError:
            print('Could not open file:', filename)
            # uhh do something? idk?

    def add_interest(self, new_interest):
        
        if new_interest in self.interests:
            print(new_interest, ' already in interests dictionary')
        else:

            # create a new dictionary and store empty dict of people mapped by email 
            people = dict(people={})

            #add new interest to interests dict
            self.interests[new_interest] = people
        
    def get_interest(self, person):
        '''given a person dict, returns the interest'''
        return person['interest']

    def get_email(self, person):
        '''given a person dict, returns the email'''
        return person['email']

    def add_person(self, person):
        '''adds person to database
           takes in person object'''

        person_dict = person.person_data_dict()

        person_interest = self.get_interest(person_dict)
        person_email = self.get_email(person_dict)

        if person_interest in self.interests:
            #if interest already exists, simply add new person to person dict
            #if person is already in person dict, should simply update info
            self.interests[person_interest]['people'][person_email] = person_dict
           
        else:
            #if interest doesnt exits yet, create new interest, addd person to person dict mapped by email
            self.add_interest(person_interest)
            self.interests[person_interest]['people'][person_email] = person_dict
    
    def format_json(self):
        '''format database dictionary into json, does not export as file though'''
        json_database = json.dumps(self.database)
        return json_database

    def export_json(self, out_filename):
        '''export database object as json file'''
        with open(out_filename, 'w') as out_file:
            json.dump(self.database, out_file)

        
