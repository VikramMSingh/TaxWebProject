from flask import Flask, render_template, request
import sys
import os
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
csrf=CsrfProtect()
csrf.init_app(app)
from routes import *


if __name__ == "__main__":
	app.secret_key='9819214251'
	app.debug = True
	app.run()
	
