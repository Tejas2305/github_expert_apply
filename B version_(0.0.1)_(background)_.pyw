from pywikihow import search_wikihow
from requests.api import options
import speech_recognition as sr
from googlesearch import search
from bs4 import BeautifulSoup
from requests import get
import pywhatkit as kt
import requests, json
import googlesearch
import numpy as np
import subprocess
import webbrowser
import wikipedia
import timetable
import speedtest
import pyautogui
import requests
import calendar
import datetime
import smtplib
import pyttsx3
import random
import time
import cv2
import sys
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

def findDay(date):
	born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
	return (calendar.day_name[born])  
from datetime import date
today = date.today()
d3 = today.strftime("%d %m %Y")
da=(d3)
d=(findDay(da))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()
       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        import datetime
        hour = int(datetime.datetime.now().hour)
        a=("meet.google.com/pyo-qzae-iec")
        
       
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)#wiki
        
        elif 'on google' in query and 'search' in query:
            query = query.replace("search", "")
            query = query.replace("on google", "")
            kt.search(query)    

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak("Opening youtube")#youtube

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("Opening gmail")#gmail 

        elif '9 de' in query or '9d' in query: 
            webbrowser.open(a) 
            speak("Opening 9D")#9d
        
        elif 'open marathi' in query:
            webbrowser.open('meet.google.com/vin-czgu-ooo')
            speak("Opening Marathi class")

        elif 'open comp' in query:
            webbrowser.open("meet.google.com/iqp-tgxx-dzu")
            speak("Opening Computer class")

        elif 'open friends' in query:
            webbrowser.open('meet.google.com/aft-woic-bgq')
            speak("Opening friends meet")#friends meet

        
        elif 'triggered insaan' in query:
            speak("Opening Triggered Insaan's channel")#triggred insaan
            webbrowser.open('https://www.youtube.com/channel/UCfLuT3JwLx8rvHjHfTymekw')

        elif 'open drive' in query:
            speak("Opening Google Drive")#drive
            webbrowser.open('https://drive.google.com/drive/my-drive')

        elif 'net speed' in query:
            wifi  = speedtest.Speedtest()
            download = wifi.download()
            upload = wifi.upload()
            print("Wifi Download Speed is ", "{:.2f}".format(download)+ "Mb/s")
            speak("Wifi Download Speed is ", "{:.2f}".format(download)+ "Mb/s")
            print("Wifi Upload Speed is ", "{:.2f}".format(upload)+ "Mb/s")
            speak("Wifi Upload Speed is ", "{:.2f}".format(upload)+ "Mb/s")

        elif 'open whatsapp' in query:
            speak("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

##################################################################################
# Mailing

        elif 'tejas' in query or 'mel tejas' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "tejas.jagdish.patil23@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'yogesh' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "imyogeshjadhav@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'ishan' in query or 'mel ishan' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "deo.ishaan123@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

##################################################################################
# Timetable

        elif 'which period' in query:
            timetable.B()       
##################################################################################
# open apps         
        
        elif 'open file explorer' in query:
            subprocess.call('explorer.exe')
            speak('Opening file explorer')#file explorer

        elif 'play music' in query:
            music_dir = 'E:\Songs'
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, song))#music
        
        elif 'open google' in query:
            speak("Opening Google")#google
            subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
            
        elif 'movies' in query:
            movie_dir = 'E:\Movies'
            os.startfile(os.path.join(movie_dir))#movie

#################################################################################
# close apps
        elif 'close google' in query:
            os.system("taskkill /im chrome.exe /f")

#################################################################################
# take a screenchot
        elif 'take screenshot' in query:
            speak("Sir, please tell me the name for this screenshot file")
            name =takeCommand().lower()
            speak("Please hold the screen for few seconds sir, I am taking screnshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"E:\Screenshots\{name}.png")
            speak("I have taken the screenshot sir. It is saved in E drive Screenshots folder. You can continue your work sir")

#################################################################################
# write a python file
        elif 'create an python file' in query:
            z = open("E:\\Neel\\Python projects\\write python file\\new.py", 'w')
            speak("Should i write in it")
            writing = takeCommand().lower()
            if 'yes' in writing:
                speak("Writing")
                s = takeCommand().lower()
                #z.save(f"E:\Neel\Python projects\write python file\{name}.py")
                z.write(s)
                z.close()
                speak("Done sir")      

#################################################################################
#How to do
        elif 'enable how to do mode' in query:
            speak("How to do mode is enabled")
            how = takeCommand().lower()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

#################################################################################
#Calculations            

        elif 'calculate' in query:
            print("Which operation should i perform?")
            speak("Which operation should i perform?")
            op = takeCommand()
            if 'addition' in op:
                speak("Tell me your First number sir?")
                print("Tell me your First number sir?")
                num1 = takeCommand()
                speak("Tell me your Second number sir?")
                print("Tell me your Second number sir?")
                num2 = takeCommand()
                speak(num1+" + " +num2 +" is " + str(int(num1)+int(num2)))
                print(num1+" + " +num2 +" is " + str(int(num1)+int(num2)))

            if 'subtract' in op:
                speak("Tell me your First number sir?")
                print("Tell me your First number sir?")
                num1 = takeCommand()
                speak("Tell me your Second number sir?")
                print("Tell me your Second number sir?")
                num2 = takeCommand()
                speak(num1+" - " +num2 +" is " +str(int(num1)-int(num2)))
                print(num1+" - " +num2 +" is " +str(int(num1)-int(num2)))

            if 'multiply' in op:
                speak("Tell me your First number sir?")
                print("Tell me your First number sir?")
                num1 = takeCommand()
                speak("Tell me your Second number sir?")
                print("Tell me your Second number sir?")
                num2 = takeCommand()
                speak(num1+" × " +num2 +" is " +str(int(num1)*int(num2)))
                print(num1+" × " +num2 +" is " +str(int(num1)*int(num2)))

            if 'divide' in op:
                speak("Tell me your First number sir?")
                print("Tell me your First number sir?")
                num1 = takeCommand()
                speak("Tell me your Second number sir?")
                print("Tell me your Second number sir?")
                num2 = takeCommand()
                speak(num1+" ÷ " +num2 +" is " +str(int(num1)/int(num2)))
                print(num1+" ÷ " +num2 +" is " +str(int(num1)/int(num2)))

#################################################################################
#Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

#################################################################################
#ip adress
        elif 'what is my ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"Your IP address is {ip}")
            speak(f"Your IP address is {ip}")

#################################################################################
#Important dates
        
        elif '26 January' in query:
            results = wikipedia.summary("Republic Day (India)", sentences=2)
            speak(results)

        elif '15 August' in query:
            results = wikipedia.summary("Independence Day (India)", sentences=2)
            speak(results)

#################################################################################
#Weather
    
        elif 'weather of' in query:
            #print("Which city you would like to know the weather of?")
            #speak("Which city you would like to know the weather of?")
            query = query.replace("weather", "")
            query = query.replace("of", "")
            CITY = query
            URL = "https://api.openweathermap.org/data/2.5/weather?"+ "q=" + CITY + "&appid=" + "90c3e5d981d5abeeb2e6d05415396cd8"
            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = (int)((int)(main['temp'])-273.15)
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                print(f"{CITY:-^30}")
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")
                print(f"Pressure: {pressure}")
                print(f"Weather Report: {report[0]['description']}")
                speak(f"Temperature: {temperature}°C")
                speak(f"Humidity: {humidity}%")
                speak(f"Pressure: {pressure}")
                speak(f"Weather Report: {report[0]['description']}")

#################################################################################
#Screen Record
        elif 'record screen' in query:
            Screen_Size = (1920, 1080)
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
#################################################################################
#bye            
            
        elif 'bye' in query and hour>=0 and hour<12:
            speak("Bye Sir!! Have a Nice Day ahead. See you afterwards")
            exit()

        elif 'bye' in query and hour>=12 and hour<18:
            speak("Bye Sir!! Have a Nice Day ahead. See you afterwards") 
            exit()

        elif 'bye' in query and hour>=18 and hour<21:
            speak("Bye Sir!! Have a Nice Day ahead. See you afterwards")
            exit()

        elif 'bye' in query and hour>=21 and hour<24:
            speak("Good Night Sir! Have a nice sleep. See you tomorrow")
            exit()


