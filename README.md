# LifeBot

## Installation
Install all dependencies
```bash
pip install -r requirements.txt
```

## Configuration
This API uses APIMEDIC Api for medical queries. To access APIMEDIC api Sign Up on <https://apimedic.com>, and set following environment variables with credentials available at <https://apimedic.com/apikeys>.

```
export username=<your_user_name>
export password=<your_api_key_password>
```

## Start the server
Start the API server using
```
python3 server.py
```

## Endpoints
- `/` - Default Page
- `/symptoms` - List of all available symptoms
- `/disease/<symptom_id>/<gender>/<year>` - Most probable disease based on given symptoms. Concatenate multiple Symptoms using `+`.  
    Example: `/disease/9+10/male/1998` returns 
    ```
    {
        "profName": "Foodborne illness", 
        "simpleName": "Food poisoning", 
        "status": "ok"
    }
    ```
- `/condition/<disease>` - Medical Conditions for given disease.  
Example: `/condition/influenza` returns  
```
{
  "details": "Flu is primarily treated with rest and fluid intake to allow the body to fight the infection on its own. Paracetamol may help cure the symptoms but NSAIDs should be avoided. An annual vaccine can help prevent the flu and limit its complications.", 
  "disease": "influenza", 
  "medications": "Decongestant, Cough medicine, Nonsteroidal anti-Inflammatory drug, Analgesic, and Antiviral drug", 
  "selfcare": "Bed rest and Throat lozenge", 
  "specialists": "Paediatrician and Primary Care Provider (PCP)", 
  "status": "ok"
}
```

- `/sentence/<text>` - Detect symptoms from text and return medical conditions.  
Example: `/sentence/I am having back pain` returns
```
{
  "details": "Not every disc needs intervention. When required, treatment includes medication, physiotherapy and possibly surgery.", 
  "disease": "disc herniation", 
  "medications": "Nonsteroidal anti-Inflammatory drug", 
  "selfcare": "Heating pad and Physical exercise", 
  "specialists": "Orthopaedic Surgeon, Physiotherapist, Neurologist, Neurosurgeon, Primary Care Provider (PCP), and Emergency Medicine Doctor", 
  "status": "ok"
}
```

- `/doctor/location` - List of all nearest doctor from Given Location  
Example: `/doctor/shaheed nagar bhubaneswar` returns
```
{
  "doctors": [
    "Das Dr Bijay Ketan", 
    "Dr J R Dash", 
    "Dr B B Nanda"
  ]
}
```

## NLP Engine
NLP Engine is hosted on Heroku and use `node-nlp` library for Natural Language Processing. It takes statement from user and returns possible symptoms over a REST API.


Endpoint: https://fathomless-ridge-45332.herokuapp.com/text=<STATEMENT_HERE>

## Chat Bot
Chat Bot is designed using Telegram Bot Wrapper

## Credits
- Google Search for finding medical conditions and nearest doctor from location.
- APIMedic API for finding disease based on Symptoms
- `node-nlp` library for Natural Language Processing
- Telegram Python Wrapper for creating chat bot for Telegram

## LICENSE
- GPLv3