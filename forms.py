from codecs import getencoder
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = StringField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])

    password = PasswordField('Password', [DataRequired()])




class ForgotForm(Form):
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class QuestionForm1(Form):
    bloodpressure = StringField('What is your Blood Pressure (mmHg)?', [DataRequired()])
    cholesterol = StringField("What is your cholesterol level (mg/dL)?", [DataRequired()])
    weight = (StringField("What is your weight (lb)?", [DataRequired()]))
    height = (StringField("What is your height (inches)?", [DataRequired()]))
    #bmi = weight/[(height)^2]
    stroke = StringField("Have you ever had a stroke in your life? (Answer Y/N)", [DataRequired()])
    heartproblems = StringField("Have you ever had heart disease or a heart attack? (Answer Y/N)", [DataRequired()])
    
class QuestionForm2(Form):
    smoker = StringField("Have you smoked 100 cigarettes in your life? (Answer Y/N)", [DataRequired()])
    physactivity = StringField("Have you taken part in Physical Activity in the past 30 days? (Answer Y/N)", [DataRequired()])
    fruits = StringField("Do you consume fruits at least 1 time per day? (Y/N)", [DataRequired()])
    veggies = StringField("Do you consume vegetables at least 1 time per day? (Y/N)", [DataRequired()])
    alcohol = StringField("If you are an adult male, do you consume more than 14 drinks per week?\n If you are an adult female, do you consume more than 7 drinks per week? (Y/N)", [DataRequired()])
    #Alcohol should in theory use the gender inputted at registering to choose between 14 or 7.

class QuestionForm3(Form):
    genhealth = StringField("On a scale of 1-5, in general your health is (with 1 being excellent, 5 being poor)", [DataRequired()])
    physhealth = StringField("In the past 30 days, how many days was your physical health not good (physical illness or injury)?", [DataRequired()])
    menthealth = StringField("In the past 30 days, how many days was your mental health not good (stress, depression, hard to control emotions)?", [DataRequired()])
    diffwalk = StringField("Do you have difficulty walking or climbing stairs? (Y/N)", [DataRequired()])

class QuestionForm4(Form):
    cholcheck = StringField("Have you had a cholesterol check in the past 5 years?", [DataRequired()])
    healthcare = StringField("Do you have any healthcare or health insurance? (Y/N)", [DataRequired()])
    noDocBecauseCost = StringField("In the past year, have you ever needed to see a doctor but have not been able to because of the cost? (Y/N)", [DataRequired()])

class QuestionForm5(Form):
    age = StringField("What is your age?", [DataRequired()])
    gender = StringField("What is your gender? (F/M)", [DataRequired()])
    education = StringField("What is the highest grade of school you have completed? Type 13 if you are a Freshman in college, 14 if Sophomore, 15 if Junior, and 16 if Senior or have completed an undergrad.", [DataRequired()])
    income = StringField("What is your annual income? Exclude the dollar sign and any commas in your response.", [DataRequired()])
    #Demographics, delete if the ability to update is added