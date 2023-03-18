from flask import Flask, render_template, jsonify, request
#from apscheduler.schedulers.background import BackgroundScheduler
import requests
from os import system
from datetime import datetime as dt
import json


#system("clear")
app = Flask(__name__)
 
def show():
  ct = dt.now()
  dict = {"year":ct.year,"month":ct.month,"day":ct.day,"hour":ct.hour,"minute":ct.minute,"second":ct.second}
  return dict

def box(sec):
    if(sec%5==0):
        return "🟥 🟩 🟨 🟦 🟪"
    elif sec%5==1:
        return "🟩 🟨 🟦  🟪 🟥"
    elif sec%5==2:
        return "🟨 🟦 🟪 🟥 🟩 "
    elif sec%5==3:
        return "🟦 🟪 🟥 🟩 🟨 "
    elif sec%5==4:
        return " 🟪 🟥 🟩 🟨 🟦"            
    
 
@app.route("/")
def index():
    tm = show()
    pattern = box(tm['second'])
    return render_template("index.html",message=tm,patt=pattern)

    
if __name__ == "__main__":
   ''' scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(chuck, "interval", seconds=15)
    '''
   app.run(debug=True)