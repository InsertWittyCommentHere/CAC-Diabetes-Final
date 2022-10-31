#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from secrets import token_bytes
from flask import Flask, render_template, request, session
import logging
from logging import Formatter, FileHandler
from forms import *
import os

import pickle
import json

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
# in order to use flask sessions, we need secret key :)
random_string = os.urandom(12).hex()
print("Secret key is: ", random_string)
app.secret_key = random_string


#----------------------------------------------------------------------------#
# RF model variable older
#----------------------------------------------------------------------------#

#   1.  HighBP                  v1          P1
# 	2.  HighChol                v2          P1
# 	3.  CholCheck               v16         P4
# 	4.  BMI	                    v3, v4      P1
#   5.  Smoker                  v7          P2
# 	6.  Stroke                  v5          P1
# 	7.  HeartDiseaseorAttack    v6          P1
# 	8.  PhysActivity            v8          P2
# 	9.  Fruits                  v9          P2
# 	10. Veggies                 v10         P2
# 	11. HvyAlcoholConsump       v11         P2
# 	12. AnyHealthcare           v17         P4
# 	13. NoDocbcCost             v18         P4
# 	14. GenHlth                 v12         P3     
# 	15. MentHlth                v13         P3
# 	16. PhysHlth                v14         P3
# 	17. DiffWalk                v15         P3
# 	18. Sex                     v20         P5
# 	19. Age                     v19         P5
# 	20. Education               v21         P5
# 	21. Income                  v22         P5

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/loginindividual', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    global username
    username = request.form.get("username")
    global password
    password = request.form.get("password")

    print(username, password)
    return render_template('forms/loginindividual.html', form=form)

@app.route('/loginofficial', methods=['GET', 'POST'])
def loginOfficial():
    form = LoginForm(request.form)
    global username
    username = request.form.get("username")
    global password
    password = request.form.get("password")

    print(username, password)
    return render_template('forms/loginhealthofficial.html', form=form)

@app.route("/dashboardindividual", methods=['GET', 'POST'])
def dashboardindividual():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        session['user'] = request.form['username']
        session['password'] = request.form['password']
        if session['user'] == "user" and session['password'] == "password":
            return render_template("pages/individualdashboard.html")
        if session['user'] == "Riyan" and session['password'] == "password":
            return render_template("pages/individualdashboard.html")
        else:
            return render_template("forms/loginindividual.html", login_err="\nLogin Failed, please try again")
    elif request.method == 'GET' and session['user'] == None or session['password'] == None:
        return render_template("forms/loginindividual.html")
    elif request.method == 'GET' and session['user'] != None or session['password'] != None:
        return render_template("pages/individualdashboard.html")
    else:
        return render_template("errors/404.html")

@app.route("/dashboardofficial", methods=['GET', 'POST'])
def dashboardofficial():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        session['user'] = request.form['username']
        session['password'] = request.form['password']
        if session['user'] == "Admin" and session['password'] == "official":
            return render_template("pages/dashboardhealthofficial.html")
        if session['user'] == "Riyan" and session['password'] == "password":
            return render_template("pages/dashboardhealthofficial.html")
        else:
            return render_template("forms/loginhealthofficial.html", login_err="\nLogin Failed, please try again")
    elif request.method == 'GET' and session['user'] == None or session['password'] == None:
        return render_template("forms/loginhealthofficial.html")
    elif request.method =='GET' and session['user'] != None or session['password'] != None:
        return render_template("pages/dashboardhealthofficial.html")
    else:
        return render_template("errors/404.html")

@app.route("/q1", methods=['GET', 'POST'])
def q1():
    if request.method == 'POST':
        # nothing really happens here cuz this won't be called.
        pass
    elif request.method == 'GET':
        print("welcome", session['user'])
        return render_template("forms/q1.html")

@app.route("/q2", methods=['GET', 'POST'])
def q2():
    if request.method == 'POST':
        # Blood Pressure, convert it to binary
        session['HighBP'] = request.form['v1']
        # Cholestrol, convert it to binary
        session['HighChol'] = request.form['v2']
        # Weight
        weight = float(request.form['v3'])
        # Height
        height = float(request.form['v4'])
        session['BMI'] = (weight / (height * height)) * 703.07
        # convert to binary
        session['Stroke'] = request.form['v5']
        # convert to binary
        session['HeartDiseaseorAttack']  = request.form['v6']
        return render_template("forms/q2.html")

    elif request.method == 'GET':
        return render_template("forms/q2.html")

@app.route("/q3", methods=['GET', 'POST'])
def q3():
    if request.method == 'POST':
        #convert to binary as applicable
        session['Smoker'] = request.form['v7']
        session['PhysActivity'] = request.form['v8']
        session['Fruits'] = request.form['v9']
        session['Veggies'] = request.form['v10']
        session['HvyAlcoholConsump'] = request.form['v11']
        return render_template("forms/q3.html")
    elif request.method == 'GET':
        return render_template("forms/q3.html")


@app.route("/q4", methods=['GET', 'POST'])
def q4():
    if request.method == 'POST':
        session['GenHlth'] = request.form['v12']
        session['MentHlth'] = request.form['v13']
        session['PhysHlth'] = request.form['v14']
        session['DiffWalk'] = request.form['v15']
        return render_template("forms/q4.html")
    elif request.method == 'GET':
        return render_template("forms/q4.html")


@app.route("/q5", methods=['GET', 'POST'])
def q5():
    if request.method == 'POST':
        session['CholCheck'] = request.form['v16']
        session['AnyHealthcare'] = request.form['v17']
        session['NoDocbcCost'] = request.form['v18']

        return render_template("forms/q5.html")
    elif request.method == 'GET':
        return render_template("forms/q5.html")


@app.route("/process", methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        print("hello")
        session['Age'] = request.form['v19']
        session['Sex'] = request.form['v20']
        session['Education'] = request.form['v21']
        session['Income'] = request.form['v22']
        print("Dumping entire session")
        print(session)
        return render_template("pages/process.html")
    


@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST' or request.method == 'GET':
        #mylist = []

        # Loading model to compare the results
        model = pickle.load( open('model.pkl','rb'))
        print(model)
        result = model.predict([[session['HighBP'],
                    session['HighChol'],
                    session['CholCheck'],
                    session['BMI'],
                    session['Smoker'],
                    session['Stroke'],
                    session['HeartDiseaseorAttack'],
                    session['PhysActivity'],
                    session['Fruits'],
                    session['Veggies'],
                    session['HvyAlcoholConsump'],
                    session['AnyHealthcare'],
                    session['NoDocbcCost'],
                    session['GenHlth'],
                    session['MentHlth'],
                    session['PhysHlth'],
                    session['DiffWalk'],
                    session['Sex'],
                    session['Age'],
                    session['Education'],
                    session['Income']]])
        #result = model.predict(data)            
        print(result)
        print(type(result))
        result_list = list(result)
        print("result_list: ", result_list)
        print(result_list[0])
        if result_list[0] == 0.0:
            resultString = "Congratulations! You do not have diabetes."
            print(result_list[0])
        if result_list[0] == 1.0:
            resultString = "Unfortunately, you have pre-diabetes. This means that your blood sugar levels are high, but not high enough to be classified as diabetes. "
            print(result_list[0])
        if result_list[0] == 2.0:
            resultString = "Unfortunately, you have diabetes."
            print(result_list[0])

        #result = model.predict([[1,1,1,40,1,0,0,0,0,1,0,1,0,5,18,15,1,0,9,4,3]])
        #print(model.predict([[0,0,0,25,1,0,0,1,0,0,0,0,1,3,0,0,0,0,7,6,1]]))
        #print(model.predict([[1,1,1,28,0,0,0,0,1,0,0,1,1,5,30,30,1,0,9,4,8]]))
        #print(model.predict([[1,0,1,27,0,0,0,1,1,1,0,1,0,2,0,0,0,0,11,3,6]]))
        #print(model.predict([[1,1,1,24,0,0,0,1,1,1,0,1,0,2,3,0,0,0,11,5,4]]))
        #print(model.predict([[1,1,1,25,1,0,0,1,1,1,0,1,0,2,0,2,0,1,10,6,8]]))
        return render_template("pages/prediction_result.html", result=resultString)

@app.route('/statGender')
def statGender():
    return render_template('pages/statGender.html')

@app.route('/statAge')
def statAge():
    return render_template('pages/statAge.html')

@app.route('/statEducation')
def statEducation():
    return render_template('pages/statEducation.html')

@app.route('/statIncome')
def statIncome():
    return render_template('pages/statIncome.html')

@app.route('/statPhysActivity')
def statPhysActivity():
    return render_template('pages/statPhysActivity.html')

@app.route('/statSmoking')
def statSmoking():
    return render_template('pages/statSmoking.html')

@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@app.route("/choose")
def choose():
    return render_template('pages/choose.html')



# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
'''
if __name__ == '__main__':
    app.run()
'''
# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 2500))
    app.run(host='0.0.0.0', port=port)

