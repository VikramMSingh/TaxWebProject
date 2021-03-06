from wtforms import TextField, BooleanField, PasswordField, SubmitField, validators, StringField, DateField, IntegerField, SelectField, RadioField
from flask.ext.wtf import FlaskForm
from flask_wtf.csrf import CsrfProtect
from wtforms.validators import DataRequired
from application import app

class registration(FlaskForm):
    csrf_token=CsrfProtect(app)		
    email=StringField('Email', [validators.DataRequired()])
    password=PasswordField('Password', [validators.DataRequired(),validators.Length(min=8, max=13),validators.EqualTo('confirm', message='Passwords must match')])
    confirm=PasswordField('Confirm password', [validators.Optional()])
    submit=SubmitField("Register")

class loginform(FlaskForm):
    csrf_token=CsrfProtect(app)
    email=StringField('Email',[validators.DataRequired()])
    password=PasswordField('Password', [validators.DataRequired()])
    submit=SubmitField('Login')

class profileform(FlaskForm):
    csrf_token=CsrfProtect(app)
    first_name=StringField('First Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    middle_name=StringField('Middle Name', [validators.Optional()])
    last_name=StringField('Last Name', [validators.Optional()])
    date_of_birth= DateField('Date of Birth', format='yyyy-dd-mm')
    address_us_line1=StringField('Street name or House number', [validators.DataRequired(), validators.length(max=200)])
    address_us_line2=StringField('Apartment', [validators.Optional()])
    city_us=StringField('City', [validators.DataRequired()])
    State_us=SelectField('State', [validators.DataRequired()], choices=[('OH', 'Ohio'), ('NY', 'New York')])
    zip_us=StringField('Zip Code', [validators.DataRequired()])
    phone_number=IntegerField('Phone Number', [validators.DataRequired(), validators.length(min=10, max=10)])
    submit=SubmitField('Done')

class nationalityform(FlaskForm):
    csrf_token=CsrfProtect(app)
    nationality=SelectField('Please select country of citizenship', [validators.DataRequired()],
                            choices=[('India', 'India'), ('China', 'China'),('Spain','Spain')])
    passport_number=StringField('Enter your passport number', [validators.DataRequired()])
    visa_type=SelectField('Visa type on entry to the US', [validators.DataRequired()], choices=[('F1', 'F1'), ('H1B', 'H1B'), ('J1', 'J1')])
    date_of_entry=DateField('First date of entry to the US', [validators.DataRequired()], format('mm-dd-yyyy'))
    travel_boolean=SelectField('Travelled outside the US within the past 3 years?', [validators.DataRequired()],
                               choices=[('Yes', 'Yes'), ('No', 'No')])
    visa_change=SelectField('Current visa status', [validators.Optional()], choices=[('F1','F1'), ('H1B','H1B'), ('J1','J1')])
    submit=SubmitField('Next')

class travel_detail(FlaskForm):
    csrf_token=CsrfProtect(app)
    start_date_1=DateField('Enter date when you left US', [validators.DataRequired()], format('mm-dd-yyyy'))
    end_date_1=DateField('Date of return', [validators.DataRequired()], format('mm-dd-yyyy'))
    start_date_2=DateField('Exit date', [validators.Optional()], format('mm-dd-yyyy'))
    end_date_2=DateField('Date of return', [validators.Optional()], format('mm-dd-yyyy'))
    start_date_3=DateField('Date of exit', [validators.Optional()], format('mm-dd-yyyy'))
    end_date_3=DateField('Date of return',[validators.Optional()], format('mm-dd-yyyy'))
    submit=SubmitField('Next')

class addressUSform(FlaskForm):
    csrf_token=CsrfProtect(app)
    address_line_1=StringField('Street number or house', [validators.DataRequired()])
    address_line_2=StringField('Address line 2', [validators.Optional()])
    city=StringField('City', [validators.DataRequired()])
    state=StringField('State',[validators.DataRequired()])
    pincode_US=StringField('Zipcode', [validators.DataRequired(), validators.length(min=4,max=8)])
    country=SelectField('Country', [validators.DataRequired()], choices=[('India', 'India'), ('China', 'China')])
    phone_foreign=StringField('Phone Number', [validators.Optional(), validators.length(min=10, max=10)])
    submit=SubmitField('Next')

class educationForm(FlaskForm):
    csrf_token=CsrfProtect(app)
    #university=SelectField('Enter the name of the educational institution', [validators.DataRequired()], choices=[(1,'Case Western'), (2,'Harvard')])
    #advisor_name=StringField('Name of advisor', [validators.DataRequired()])
   # advisor_phone=IntegerField('Advisor phone number', [validators.DataRequired(), validators.length(min=8, max=10)])
  #  uni_phone=IntegerField('University phone', [validators.DataRequired(), validators.length(min=8, max=10)])
    submit=SubmitField('Next')

class maritalForm(FlaskForm):
    csrf_token=CsrfProtect(app)
    marital_status=RadioField('', [validators.Optional()], choices=[('Married', 'Married')])
    single_status=RadioField('', [validators.Optional()], choices=[('Single', 'Single')])
    dependent=RadioField('Do you claim your wife as a dependent?', [validators.Optional()],choices=[('Yes', 'Yes'), ('No', 'No')])
    kidsNumber=IntegerField('Number of kid/kids', [validators.Optional()])
    submit=SubmitField('Next')

class financialForms(FlaskForm):
    csrf_token=CsrfProtect(app)
    W2form=IntegerField('Number of W2 forms', [validators.Optional()])
    DivForm=IntegerField('Number of 1099-Div forms', [validators.Optional()])
    IntForm=IntegerField('Number of 1099-Int forms', [validators.Optional()])
    StatusForm=IntegerField('Number of 1099-B forms', [validators.Optional()])
    S1042Form=IntegerField('Number of 1042-S forms', [validators.Optional()])
    TForm=IntegerField('Number of 1098-T forms', [validators.Optional()])
    MiscForm=IntegerField('Number of 1099-Misc forms', [validators.Optional()])
    submit=SubmitField('Next')