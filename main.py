from flask import Flask, render_template , url_for,request,redirect,send_file
from datetime import datetime
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
from pyqrcode import QRCode
import pyqrcode
import png
import os

app = Flask(__name__)


@app.route("/check_number")
def checknuber():
    return render_template("check_number.html")

@app.route("/check", methods = ['POST','GET'])
def check():
    if request.method == 'POST' :
        
        code = request.form.get('code')
        mobile = request.form.get('number')

        user_no = f"+{code}{mobile}"
        phoneNumber = phonenumbers.parse(user_no)
        valid = phonenumbers.is_valid_number(phoneNumber)

        if valid : 
            timeZone = timezone.time_zones_for_number(phoneNumber)
            Carrier = carrier.name_for_number(phoneNumber, 'en')
            Region = geocoder.description_for_number(phoneNumber, 'en')
            # data = {"Number":str(phoneNumber),"Time Zone" : timeZone,"Carrier" : Carrier,"Location" : Region}
            return f"Number : {phoneNumber}<br>Time Zone : {timeZone}<br>Carrier : {Carrier}<br>Location : {Region}"
        else:
            return "Please enter a valid number"
        
@app.route("/qr")
def qr():
    return render_template("qr.html")   

@app.route("/create_qr",methods = ['POST','GET'])
def create_qr():
    if request.method == 'POST' :
        link = request.form.get('Link')
        qr_ready = pyqrcode.create(link)
        qr_ready.png('static\images\myqr.png', scale = 6)
        path = "static\images\myqr.png"
    
    return send_file(path,as_attachment=True)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)
