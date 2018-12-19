let express = require('express');
var app = express();


const { NlpManager } = require('node-nlp');


const manager = new NlpManager({ languages: ['en'] });
var arr = [];
// Adds the utterances and intents for the NLP
//back pain
manager.addDocument('en', 'back pain', 'back pain');
manager.addDocument('en', 'back is aching', 'back pain');
manager.addDocument('en', 'back aches', 'back pain');
manager.addDocument('en', 'my back is hurting', 'back pain');

// Abdominal
manager.addDocument('en', 'Abdominal pain', 'abdominal pain');
manager.addDocument('en', 'stomach ache', 'abdominal pain');
manager.addDocument('en', 'abdominal hurts', 'abdominal pain');

// Anxiety
manager.addDocument('en', 'anxiety', 'anxiety');
manager.addDocument('en', 'sleep problems', 'anxiety');
manager.addDocument('en', 'difficulty in falling or staying asleep', 'anxiety');
manager.addDocument('en', 'difficulty concentrating', 'anxiety');
manager.addDocument('en', 'mind is going blank', 'anxiety');

//Chest pain
manager.addDocument('en', 'pain in my chest', 'chest pain');
manager.addDocument('en', 'chest hurts', 'chest pain');
manager.addDocument('en', 'chest ache', 'chest pain');

//Cold Sweat
manager.addDocument('en', 'cold sweat.', 'cold sweat');
manager.addDocument('en', 'concurrent perspiration', 'cold sweat');

//Cough
manager.addDocument('en', 'cough', 'Cough');
manager.addDocument('en', 'got cough from cold', 'Cough');

//Dry eyes
manager.addDocument('en', 'burning sensation in eyes', 'dry eyes');
manager.addDocument('en', 'scratchy sensation in eyes', 'dry eyes');
manager.addDocument('en', 'Stringy mucus in or around your eyes', 'dry eyes');
manager.addDocument('en', 'eye are stinging', 'dry eyes');

//Eyes pain
manager.addDocument('en', 'eyes are hurting', 'eyes pain');
manager.addDocument('en', 'eyes are paining', 'eyes pain');
manager.addDocument('en', 'eyes are aching', 'eyes pain');


//weakness//
manager.addDocument('en', 'feeling fragile', 'weakness');
manager.addDocument('en', 'feeling weak', 'weakness');
manager.addDocument('en', 'feeling powerless', 'weakness');

//Tiredness//
manager.addDocument('en', 'feeling fatigued', 'Tiredness');
manager.addDocument('en', 'energy deficient', 'Tiredness');
manager.addDocument('en', 'feel lazy', 'Tiredness');
manager.addDocument('en', 'dont have energy ', 'Tiredness');
manager.addDocument('en', ' exhausted', 'Tiredness');

//Vomitted//
manager.addDocument('en', 'vomitted ', 'Vomiting');
manager.addDocument('en', 'vomitting', 'Vomiting');
manager.addDocument('en', 'puked', 'Vomiting');
manager.addDocument('en', 'thrown up', 'Vomiting');



//Sweating//
manager.addDocument('en', 'sweating a lot', 'Sweating');
manager.addDocument('en', 'sweating a bit too much', 'Sweating');
manager.addDocument('en', 'sweating profusely', 'Sweating');



//Stuffy Nose//
manager.addDocument('en', ' stuffy nose', 'Stuffy nose');
manager.addDocument('en', 'nose is running', 'Stuffy nose');
manager.addDocument('en', 'running nose', 'Stuffy nose');
manager.addDocument('en', 'inflammed nose', 'Stuffy nose');
manager.addDocument('en', 'nasal congestion', 'Stuffy nose');
manager.addDocument('en', 'nose is blocked', 'Stuffy nose');
manager.addDocument('en', 'blocked nose', 'Stuffy nose');
manager.addDocument('en', 'nostril is blocked', 'Stuffy nose');
manager.addDocument('en', 'cant breathe through my nose ', 'Stuffy nose');
manager.addDocument('en', 'nose is clogged up', 'Stuffy nose');



//Gaining Weight//
manager.addDocument('en', 'gaining weight', 'Weight gain');
manager.addDocument('en', 'weight is increasing','Weight gain');
manager.addDocument('en', 'putting on weight', 'Weight gain');
manager.addDocument('en', 'gaing weight rapidly', 'Weight gain');

//Earache//
manager.addDocument('en', 'ear pain', 'Earache');
manager.addDocument('en', 'ear hurts','Earache');
manager.addDocument('en', 'ear ache', 'Earache');
manager.addDocument('en', 'eareache', 'Earache');
manager.addDocument('en', 'ear infection', 'Earache');

//Fast, deepened breathing
manager.addDocument('en', 'Fast, deepened breathing', 'Fast, deepened breathing');
manager.addDocument('en', 'deepened breathing', 'Fast, deepened breathing');
manager.addDocument('en', 'Fast breathing', 'Fast, deepened breathing');
manager.addDocument('en', 'Shortness of breath', 'Fast, deepened breathing');
manager.addDocument('en', 'suffocating', 'Fast, deepened breathing');
manager.addDocument('en', 'Asphyxia', 'Fast, deepened breathing');
manager.addDocument('en', 'losing breath', 'Fast, deepened breathing');

//Fever
manager.addDocument('en', 'Fever', 'Fever');
manager.addDocument('en', 'high temprature', 'Fever');
manager.addDocument('en', 'Feverish', 'Fever');

//Headache
manager.addDocument('en', 'head pain', 'Headache');
manager.addDocument('en', 'head hurts','Headache');
manager.addDocument('en', 'head ache', 'Headache');
manager.addDocument('en', 'Headache', 'Headache');
manager.addDocument('en', 'Temple hurts','Headache');
manager.addDocument('en', 'Temple is aching', 'Headache');
manager.addDocument('en', 'forehead is paining', 'Headache');
manager.addDocument('en', 'forehead hurts','Headache');
manager.addDocument('en', 'forehead is aching', 'Headache');

//Increased thirst
manager.addDocument('en', 'Increased thirst', 'Increased thirst');
manager.addDocument('en', 'drinking more water', 'Increased thirst');
manager.addDocument('en', 'having more water', 'Increased thirst');
manager.addDocument('en', 'more Thirsty', 'Increased thirst');

//Itching in the nose
manager.addDocument('en', 'Itching  nose', 'Itching in the nose');
manager.addDocument('en', 'tickling nose', 'Itching in the nose');
manager.addDocument('en', 'stinging nose', 'Itching in the nose');

//Lip Swelling
manager.addDocument('en', 'Lips are swelling', 'Lip swelling');
manager.addDocument('en', 'Lips are puffy', 'Lip swelling');
manager.addDocument('en', 'Lips are bulging', 'Lip swelling');
manager.addDocument('en', 'Lips are inflammed', 'Lip swelling');

// //Missed period
// manager.addDocument('en', 'Missed period', 'Missed period');
// manager.addDocument('en', 'not having period', 'Missed period');
// manager.addDocument('en', 'didnt have period', 'Missed period');


//Neck pain
manager.addDocument('en', 'Neck is paining', 'Neck pain');
manager.addDocument('en', 'Neck hurts', 'Neck pain');
manager.addDocument('en', 'Neck is aching', 'Neck pain');

//Paralysis
manager.addDocument('en', 'Paralysis', 'Paralysis');
manager.addDocument('en', 'cant move ', 'Paralysis');
manager.addDocument('en', 'cant sense body ', 'Paralysis');

//Skin Rash
manager.addDocument('en', 'rashes on skin', 'Skin rash');
manager.addDocument('en', 'skin is itching', 'Skin rash');
manager.addDocument('en', 'feels like scatching my body', 'Skin rash');

//sneezing
manager.addDocument('en', 'Sneezing', 'Sneezing');
//Sore Throat
manager.addDocument('en', 'Sore throat', 'Sore throat');
manager.addDocument('en', 'throat is aching', 'Sore throat');
manager.addDocument('en', 'throat hurts', 'Sore throat');
manager.addDocument('en', 'inflammed throat', 'Sore throat');
manager.addDocument('en', 'throat infection', 'Sore throat');

// Train also the NLG
manager.addAnswer('en', 'back pain', 'Back pain');
manager.addAnswer('en', 'abdominal pain', 'Abdominal pain');
manager.addAnswer('en', 'anxiety', 'Anxiety');
manager.addAnswer('en', 'chest pain', 'Chest pain');
manager.addAnswer('en', 'cold sweat', 'Cold sweat');
manager.addAnswer('en', 'Cough', 'Cough');
manager.addAnswer('en', 'Vomiting', 'Vomiting');
manager.addAnswer('en', 'Weight gain', 'Weight gain');
manager.addAnswer('en', 'Tiredness', 'Tiredness');
manager.addAnswer('en', 'Sweating', 'Sweating');
manager.addAnswer('en', 'Stuffy nose', 'Stuffy nose');
manager.addAnswer('en', 'Earache', 'Earache');
manager.addAnswer('en', 'Fast, deepened breathing', 'Fast, deepened breathing');
manager.addAnswer('en', 'Fever', 'Fever');
manager.addAnswer('en', 'Headache', 'Headache');
manager.addAnswer('en', 'Increased thirst', 'Increased thirst');
manager.addAnswer('en', 'Itching in the nose', 'Itching in the nose');
manager.addAnswer('en', 'Lip swelling', 'Lip swelling');
manager.addAnswer('en', 'Missed period', 'Missed period');
manager.addAnswer('en', 'Neck pain', 'Neck pain');
manager.addAnswer('en', 'Skin rash', 'Skin rash');
manager.addAnswer('en', 'Sneezing', 'Sneezing');
manager.addAnswer('en', 'Sore throat', 'Sore throat');






// Train and save the model.
var url = "";
app.get('/:query',function (req,res) {
   var ques = req.params.query;
    (async() => {
        await manager.train();
        manager.save();
        const response = await manager.process('en', ques);
        console.log("Response");
    //    console.log(response);
        var ans = [];
       // ans = response.classification;
        var lpo = response.classification;

        for(let i = 0;i<2;i++){
            var jp = lpo[i].value;
            if(i==0 && jp>=0.1){
                console.log(lpo[i]);
                ans.push(lpo[i]);
            }else if(i==0 &&jp<0.1){
                res.send(JSON.stringify(ans));
                res.end();
                return;
            }else{
                if(jp>=0.1 && (-jp+lpo[i-1].value)<0.18){
                    console.log(-jp+lpo[i-1].value);
                    ans.push(lpo[i])
                }
            }
        }
        // response.classification.forEach(function (i) {
        //     if(i.value>0.1 && ){
        //         console.log("i");
        //         console.log(i);
        //         ans.push(i);
        //     }
        // });
     //   console.log(ans);
        var len = ans.length;
     //   ans = JSON.stringify(ans);
        var finalres =
            {data:ans,
             size: len
            };

        res.send(JSON.stringify(finalres));
        res.end();
        return;
    })();
});



app.listen(7000);
/*
Iron+deficiency+causes+anemia,+which+results+in+tiredness+and+shortness+of+breath+because+of+poor+oxygen+delivery.
 */
//https://fathomless-ridge-45332.herokuapp.com/text=I+am+having+back+pain+and+fever