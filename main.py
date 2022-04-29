from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import render_template, request
import easy_pyttsx3 as pt
import sys, webbrowser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])  
def weather():
    location=""
    time=""
    info=""
    weather=""
    city=""
    a=""
    if request.method == 'POST' and 'city' in request.form:
        city = request.form.get('city')
        city = city+"weather" 
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()

        pt.say(text='hello ')
        pt.say(text='         ')
        pt.say(text='Place '+location)
        
        pt.say(text='Weather is'+info)
        
        pt.say(text='temperature is '+weather)
        pt.say(text='° celsius')
        inf=to_tamil(info)
        pt.say(text='Now in tamil')
        pt.say(text='Vann aakkam')
        pt.say(text='         ')
        pt.say(text='Iddamm '+location)
        pt.say(text='Vaannnilai is ' + inf)
        pt.say(text='Vepppa nilllaaai'+weather)
        pt.say(text='° celsius') 
        print(inf)
        a='https://www.google.com/maps/place/' + location
    return render_template("index.html",l=location,t=time,i=info,w=weather,ap=a)

def to_tamil(info):
    if info=="Cloudy":
        info="Meekamuuutttam"
    elif info=="Partly cloudy":
        info="Oraallaaavu meekamuutttam"
    elif info=="Rainy":
        info="Mallaai"
    elif info=="Sunny":
        info="Cuuriyann tiinnttum"
    elif info=="Clear":
        info="Teli  vanna kaalaanillai"
    elif info=="Mostly sunny":
        info="Perumpaallumm veyil"
    elif info=="Haze":
        info="Muutu pani"
    return info

   
app.run()