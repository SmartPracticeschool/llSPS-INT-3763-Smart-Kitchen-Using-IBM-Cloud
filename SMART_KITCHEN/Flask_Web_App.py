import requests
import json
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import requests
from time import time
from random import random
from flask import Flask, render_template, make_response

def ltos(s):
    str1=" "

    return (str1.join(s))

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index_.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    
    r=requests.get("https://node-red-ekrbu-2020-09-04.eu-gb.mybluemix.net/data")
    dat=r.json()
    #print(dat)
    #print(type(dat))
    lis=list(dat.values())
    sng=ltos(lis)
    jar_=int(sng[0:4])
    cylinder_=float(sng[5:9])
  
    data = [time() * 1000, jar_,cylinder_]
    print(data)
    
   
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

if __name__ == "__main__":
    app.run(debug=True)
