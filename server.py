from flask import Flask, jsonify, redirect
from symptoms import HealthCare
app = Flask (__name__)

# Client for API requests
client = HealthCare()


######################
#       INDEX        #
######################

@app.route ('/', methods=['GET'])
def defaultRoute () :
    return jsonify({
		'author' : 'Aman Pratap Singh',
		'email' : 'amanprtpsingh@gmail.com',
        'endpoints': ['symptoms, disease, condition, sentence, doctor'],
        'docs': "https://github.com/apsknight/apscare"
	})

######################
#     Symptoms       #
######################

@app.route ('/symptoms', methods=['GET'])
def symptomsRoute () :
	result = client.getSymptoms()
	return jsonify (result)

######################
#       Disease      #
######################

@app.route ('/disease/<sid>/<gender>/<year>', methods=['GET'])
def diseaseRoute (sid, gender, year) :
    ids = str(sid).replace('+', ' ')
    result = client.getDiseasefromSymptoms(ids, gender, year)
	
    return jsonify (result)

######################
#       Condition    #
######################

@app.route ('/condition/<disease>', methods=['GET'])
def conditionRoute (disease) :
    disease = str(disease).replace('+', ' ')
    disease = str(disease).replace('%20', ' ')
    result = client.getConditonfromDisease(disease)
    return jsonify (result)

######################
#       Condition    #
######################

@app.route ('/sentence/<text>', methods=['GET'])
def textRoute (text) :
    text = str(text).replace('+', ' ')
    text = str(text).replace('%20', ' ')
    result = client.getConditionfromText(text)
    return jsonify (result)

######################
#       Doctor       #
######################

@app.route ('/doctor/<location>', methods=['GET'])
def doctorRoute (location) :
    location = str(location).replace('+', ' ')
    location = str(location).replace('%20', ' ')
    result = client.getNearestDoctor(location)
    return jsonify ({"doctors": result})



######################
#         404        #
######################
@app.route('/<path:dummy>')
def fallback(dummy):
    return redirect("/")


######################
#    START FLASK     #
######################

if __name__ == "__main__":
	app.run()