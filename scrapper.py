import requests
from bs4 import BeautifulSoup

# Fake USER AGENT for Google Search
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

class GoogleScrapper:

    @staticmethod
    def getTreatment(disease):
        '''
        Search disease treatment from Google Search
        '''
        disease = disease.replace(' ', '+')
        url = 'http://www.google.com/search?q={0}+treatment'.format(disease)
        result = requests.get(url, headers=USER_AGENT)
        page = result.text

        soup = BeautifulSoup(page, 'html.parser')
        try:
            details = soup.find('div', attrs={'class': 'K9xsvf Uva9vc kno-fb-ctx'}).text
        except AttributeError:
            details = "NA"
        try:
            selfcare = soup.find(text="Self-care").findNext('div').text
        except AttributeError:
            selfcare = "NA"
        try:
            medications = soup.find(text="Medications").findNext('div').text
        except AttributeError:
            medications = "NA"
        try:
           specialists = soup.find(text="Specialists").findNext('div').text
        except AttributeError:
            specialists = "NA"
            
        disease = disease.replace('+', ' ')
        result = {
            "disease": disease,
            "details": details,
            "selfcare": selfcare,
            "medications": medications,
            "specialists": specialists
            }

        return result


    @staticmethod
    def getDoctor():
        '''
        Search Nearest Doctor from location using Google Search
        '''
        url = 'http://www.google.com/search?q=doctor+nearby+me'
        result = requests.get(url, headers=USER_AGENT)
        page = result.text   

        soup = BeautifulSoup(page, 'html.parser')
        doctors = soup.findAll('div', attrs={'class': 'dbg0pd'})

        result = list()
        for doctor in doctors:
            result.append(doctor.text)

        return result