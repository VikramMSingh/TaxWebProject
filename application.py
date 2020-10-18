from flask import Flask, render_template, request, Blueprint, abort
import sys
import os
from flask_wtf.csrf import CsrfProtect
from dbconnect import connection





app = Flask(__name__)
csrf=CsrfProtect()
csrf.init_app(app)


from routes import *



if __name__ == "__main__":
	app.secret_key='9xxxxx'
	app.debug = True
	app.run()

	
