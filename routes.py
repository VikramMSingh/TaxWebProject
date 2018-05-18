from flask import Flask, render_template, request, redirect, url_for, session
import sys
import os
from flask_wtf import *
from application import app
#from wtforms import *
from passlib.hash import sha256_crypt, cisco_type7
from forms import *
from datetime import *
from dbconnect import connection
from pymysql import escape_string as thwart
import pymysql.cursors


#Landing page for website
@app.route('/')
def homepage():
	return render_template("test_page.html");	
#Registration page
@app.route('/Register', methods=['GET', 'POST'])
def register():
    try:
        form=registration(request.form)
        if request.method=='POST' and form.validate_on_submit():
            email=form.email.data
            password=sha256_crypt.encrypt((str(form.password.data)))
            c, conn=connection()

            x=c.execute('Select * FROM USERS where email=%s', (thwart(email)))

            if int(x)>0:
                flash('User already exists')
                return render_template('Registration.html', form=form)
            else:
                c.execute('Insert into USERS (email, password) VALUES (%s, %s)',
                          (thwart(email), thwart(password)))
                conn.commit()
                flash('Thanks for registering')
                c.close()
                conn.close()

                session['logged_in'] = True
                session['email'] = email


        return render_template('Registration.html', form=form)
    except Exception as e:
        return (str(e));

#login page#
@app.route('/Login', methods=['GET', 'POST'])
def login():
    try:
        form=loginform(request.form)
        if request.method=='POST' and form.validate_on_submit():
            email=request.form['email']
            password=request.form['password']
            c, conn=connection()
            data=c.execute('Select * from USERS where email=(%s)',(thwart(email)))
            data=c.fetchone()[2]

            #Password verification for user
            if sha256_crypt.verify(password, data):
                session['logged_in'] = True
                session['email'] = request.form['email']
                return redirect(url_for('dashboard'))

            else:
                error="Invalid credentials, try again"
        return render_template('LoginPage.html', form=form)
    except Exception as e:
        return (str(e));

@app.route('/Dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

#Userprofile - Name, DOB
@app.route('/Dashboard/Basic_profile', methods=['GET', 'POST'])
def Basic_profile():
    try:
        form=profileform(request.form)
        if request.method=='POST' and form.validate_on_submit():
            first_name=request.form('first_name')
            middle_name=request.form('middle_name')
            last_name=request.form('last_name')
            date_of_birth=request.form('date_of_birth')


        return render_template('User_profile.html', form=form)
    except Exception as e:
        return (str(e));

#For users that need to file form 1040NR, 1040NR-EZ, form 8843 and respective state taxes
#First page passport, nationality, year of tax filing and visa type
@app.route('/Dashboard/Taxes/page1', methods=['GET', 'POST'])
def taxes():
    try:
        form=nationalityform(request.form)
        if request.method=='POST' and form.validate_on_submit():
            nationality=request.form('nationality')
            passport_number=request.form('passport_number')
            visa_type=request.form('visa_type')
            date_of_entry=request.form('date_of_entry')
            travel_boolean=request.form('travel_boolean')
            visa_change=request.form('visa_change')



        return render_template('Nationality.html', form=form)
    except Exception as e:
        return (str(e));

@app.route('/Dashboard/Taxes/page1_travel', methods=['GET', 'POST'])
def page1_travel():
    try:
        form=travel_detail(request.form)
        if request.method=='POST' and form.validate_on_submit():
            start_date_1=request.form('start_date_1')
            end_date_1=request.form('end_date_1')

        return render_template('TravelDetail.html', form=form)
    except Exception as e:
        return (str(e));

#Second page address and phone in US
@app.route('/Dashboard/Taxes/page2', methods=['GET', 'POST'])
def page2():
    try:
        form=addressUSform(request.form)
        if request.method=='POST' and form.validate_on_submit():
            address_line_1=request.form('address_line_1')
            address_line_2=request.form('address_line_2')
            city=request.form('city')
            state=request.form('state')
            pincode_US=request.form('pincode_US')

        return render_template('addressUS.html', form=form)
    except Exception as e:
        return (str(e));

@app.route('/Dashboard/Taxes/page3', methods=['GET', 'POST'])
def education():
    try:
        form=educationForm(request.form)
        if request.method=='POST' and form.validate_on_submit():
            university=request.form('university')
            advisor_name=request.form('advisor_name')
            advisor_phone=request.form('advisor_phone')
            uni_address_1=request.form('uni_address_1')
            uni_city=request.form('uni_city')
            uni_state=request.form('uni_state')
            uni_pincode=request.form('uni_pincode')
            uni_country=request.form('uni_country')
            uni_phone=request.form('uni_phone')
        return render_template('education.html', form=form)
    except Exception as e:
        return (str(e));

@app.route('/Dashboard/Taxes/page4', methods=['GET', 'POST'])
def personal_info():
    try:
        form=maritalForm(request.form)
        if request.method=='POST' and form.validate_on_submit():
            marital_status=request.form['married']
            #single_status=request.form['single_status']
            dependent=request.form['dependent']
        return render_template('marital_form.html', form=form)
    except Exception as e:
        return (str(e));

