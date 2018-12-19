import apidemic
import scrapper
# import database
import config
import json
import requests
import ast

class HealthCare:

    def __init__ (self):
        '''
        Main Singleton object to connect with apimedic API and respond all 5 APIs endpoints
        '''
        # Retrieve username
        username = config.username
        # Retrieve password
        password = config.password

        authUrl = config.priaid_authservice_url
        healthUrl = config.priaid_healthservice_url
        language = config.language
        self._printRawOutput = config.pritnRawOutput
        
        # APIMEDIC Diagnosis Client
        self._diagnosisClient = apidemic.DiagnosisClient(username, password, authUrl, language, healthUrl)
        
        # List of all available symptoms from Apimedic API.
        self.availableSymptoms = self._diagnosisClient.loadSymptoms()

        # Client for database transactions and requests
        # self._databaseClient = database.Database()

    def getSymptoms (self):
        '''
        Return dictionary of all (ID, Name) pairs from apimedic api.
        '''
        result = dict()
        for symptom in self.availableSymptoms:
            result[symptom['ID']] = symptom['Name']

        return result

    def getDiseasefromSymptoms (self, id, gender, year):
        '''
        Params: 
            id: IDs of all possible symptoms to patient concatenated by '+'
            gender: Gender of patient (male/female)
            Year: DOB Year of patient
        '''
        gender = gender.lower()

        # Replace + with space
        id = id.replace('+', ' ')
        ids = id.split()

        # Check if all ids are integer
        for num in ids:
            if not num.isdigit():
                print('a' + num)
                return {
                    "status": "error",
                    "error": "ID should be Integers"
                }
        
        # Check if gender is valid
        if gender not in ['male', 'female']:
            return {
                    "status": "error",
                    "error": "Gender should be either male or female"
                }

        # Check if year is valid
        if not year.isdigit():
            return {
                "status": "error",
                "error": "Invalid Year"
            }

        # List of all possible diseases
        user_diagnosis = self._diagnosisClient.loadDiagnosis(id, gender, year)

        # Chose most probable (accurate) disease
        profName = user_diagnosis[0]['Issue']['ProfName']
        simpleName = user_diagnosis[0]['Issue']['Name']

        result = {
            "status": "ok",
            "profName": profName,
            "simpleName": simpleName
        }

        return result

    def getConditonfromDisease(self, disease):
        disease = disease.lower()

        # Search for disease condition's in database.
        # db_result = self._databaseClient.search(disease)
        db_result = None

        if db_result:
           result = db_result
        else:
            # If not found in database, Scrap the info from Google Search
            result = scrapper.GoogleScrapper.getTreatment(disease)
            if result:
                # Put info in database for futuee use
                # self._databaseClient.insert(result['disease'], result['details'],
                # result['selfcare'], result['medications'], result['specialists'])
                pass
        
        result['status'] = 'ok'

        return result

    def getConditionfromText(self, text):
        found_symptoms = ""
        text = text.replace(' ', '+')
        url = 'https://fathomless-ridge-45332.herokuapp.com/text={}'.format(text)
        USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        result = requests.get(url, headers=USER_AGENT)
        page = ast.literal_eval(result.text)
        # Concatenate all symptoms present in text
        for symptom in self.availableSymptoms:
            for el in page:
                if symptom['Name'].lower() == el["label"].lower():
                    found_symptoms += ' ' + str(symptom['ID'])


        found_symptoms = found_symptoms.strip()

        # If no system is found, return error
        if len(found_symptoms) == 0:
            return {
                'status': 'error',
                'error': 'No Symptom matched with given text.'
            }

        # Check disease from symptoms (Gender default to male, Year default to 1998)
        disease = self.getDiseasefromSymptoms(found_symptoms, 'male', '1998')
        
        result = self.getConditonfromDisease(disease['profName'])

        return result

    def getNearestDoctor(self):
        # Scrap Google for nearest doctors from Location
        return scrapper.GoogleScrapper.getDoctor()