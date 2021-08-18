#Importing the libraries
from flask import Flask, render_template, request
import pickle

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open("placement.pkl", "rb"))

#User-defined functions

@app.route("/", methods=["GET"])
def Home():
    return render_template("placement.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    Secondary_School_Percentage = float(request.form['Secondary School Percentage'])
    High_School_Percentage = float(request.form['High School Percentage'])
    Degree_Percentage = float(request.form['Degree Percentage'])
    e_test_Percenatege = float(request.form['e_test Percenatege'])
    MBA_percentage = float(request.form['MBA percentage'])
    gender = request.form['gender']
    Feild_of_Education = request.form['education']
    Specialisation = request.form['Specialisation']
    Work_Experience = request.form['experience']
    Subject = request.form['Subject']
    Commerce=0
    Science= 0 
  

    if gender == 'M':
        gender = 1
    else:
        gender = 0

    if Feild_of_Education == 'Comm&Mgmt':
        Feild_of_Education = 2
    elif Feild_of_Education == 'Sci&Tech':
        Feild_of_Education = 1
    else:
        Feild_of_Education = 0

    if Specialisation == 'Mkt&Fin':
        Specialisation = 1
    else:
        Specialisation = 0

    if Work_Experience == 'Yes':
        Work_Experience = 1
    else:
        Work_Experience = 0

    if Subject == "Commerce":
       Commerce = 1
       Science  = 0
    elif Subject == "Science":
       Commerce = 0
       Science  = 1
    else:
        Commerce = 0
        Science = 0
    prediction = loadedModel.predict([[Secondary_School_Percentage, High_School_Percentage, Degree_Percentage,Feild_of_Education, e_test_Percenatege,Specialisation, MBA_percentage, gender, Commerce, Science, Work_Experience]])[0]
    
    if prediction == 0:
        prediction = "Not placed"
    else:
        prediction = "Placed"

    return render_template("placement.html",output=prediction)


#Main function
if __name__ == "__main__":
    app.run(debug=True)