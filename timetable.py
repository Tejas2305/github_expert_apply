import pyttsx3
import time
import datetime
import webbrowser
import calendar

hour = int(datetime.datetime.now().hour)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def findDay(date):
	born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
	return (calendar.day_name[born])  
from datetime import date
today = date.today()
d3 = today.strftime("%d %m %Y")
da=(d3)
d=(findDay(da))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def D():

        if hour>=9 and hour<10 and d == ('Monday'):
            speak("Physics period")

        elif hour>=10 and hour<11 and d == ('Monday'):
            speak("Math period")

        elif hour>=11 and hour<12 and d==('Monday'):
            speak("Marathi period")
            webbrowser.open("meet.google.com/vin-czgu-ooo")

        elif hour>=12 and hour<13 and d==('Monday'):
            speak("Computer period")
            webbrowser.open("meet.google.com/iqp-tgxx-dzu")

        elif hour>=13 and hour<14 and d==('Monday'):
            speak("Chemistery period")

        elif hour>=9 and hour<10 and d==('Tuesday'):
            speak("Biology period")

        elif hour>=10 and hour<11 and d==('Tuesday'):
            speak("Computer period")
            webbrowser.open("meet.google.com/iqp-tgxx-dzu")

        elif hour>=11 and hour<12 and d==('Tuesday'):
            speak("GK or Ls period")
            
        elif hour>=12 and hour<13 and d==('Tuesday'):
            speak("Physics period")

        elif hour>=13 and hour<15 and d==('Tuesday'):
            speak("Geography period")
            
        elif hour>=9 and hour<10 and d==('Wednesday'):
            speak("History period")

        elif hour>=10 and hour<11 and d==('Wednesday'):
            speak("English Literature period")

        elif hour>=11 and hour<12 and d==('Wednesday'):
            speak("Biology period")
            
        elif hour>=12 and hour<13 and d==('Wednesday'):
            speak("Chemistry period")
            
        elif hour>=13 and hour<15 and d==('Wednesday'):
            speak("Physics period")  

        elif hour>=9 and hour<10 and d==('Thursday'):
            speak("Marathi period")
            webbrowser.open("meet.google.com/vin-czgu-ooo")

        elif hour>=10 and hour<11 and d==('Thursday'):
            speak("Computer period")
            webbrowser.open("meet.google.com/iqp-tgxx-dzu")

        elif hour>=11 and hour<12 and d==('Thursday'):
            speak("History period")
            
        elif hour>=12 and hour<13 and d==('Thursday'):
            speak("English Language period")
            
        elif hour>=13 and hour<15 and d==('Thursday'):
            speak("Maths period")  

        elif hour>=9 and hour<10 and d==('Friday'):
            speak("English Literature period")

        elif hour>=10 and hour<11 and d==('Friday'):
            speak("Geography period")

        elif hour>=11 and hour<12 and d==('Friday'):
            speak("History period")
            
        elif hour>=12 and hour<13 and d==('Friday'):
            speak("Maths period")
            
        elif hour>=13 and hour<15 and d==('Friday'):
            speak("Marathi period")
            
        else:
            speak("No period now")

################################################################################

def B():

        if hour>=9 and hour<10 and d == ('Monday'):
            speak("Geography period")

        elif hour>=10 and hour<11 and d == ('Monday'):
            speak("English Language period")

        elif hour>=11 and hour<12 and d==('Monday'):
            speak("Group A period")

        elif hour>=12 and hour<13 and d==('Monday'):
            speak("Group C period")

        elif hour>=13 and hour<14 and d==('Monday'):
            speak("Physics period")

        elif hour>=9 and hour<10 and d==('Tuesday'):
            speak("Chemistry period")

        elif hour>=10 and hour<11 and d==('Tuesday'):
            speak("Group C period")

        elif hour>=11 and hour<12 and d==('Tuesday'):
            speak("Math period")
            
        elif hour>=12 and hour<13 and d==('Tuesday'):
            speak("Physics period")

        elif hour>=13 and hour<15 and d==('Tuesday'):
            speak("Geography period")
            
        elif hour>=9 and hour<10 and d==('Wednesday'):
            speak("Physics period")

        elif hour>=10 and hour<11 and d==('Wednesday'):
            speak("Math period")

        elif hour>=11 and hour<12 and d==('Wednesday'):
            speak("History period")
            
        elif hour>=12 and hour<13 and d==('Wednesday'):
            speak("Chemistry period")
            
        elif hour>=13 and hour<15 and d==('Wednesday'):
            speak("English Litrature period")  

        elif hour>=9 and hour<10 and d==('Thursday'):
            speak("Group A period")

        elif hour>=10 and hour<11 and d==('Thursday'):
            speak("Group C period")

        elif hour>=11 and hour<12 and d==('Thursday'):
            speak("Biology period")
            
        elif hour>=12 and hour<13 and d==('Thursday'):
            speak("History period")
            
        elif hour>=13 and hour<15 and d==('Thursday'):
            speak("English Litrature period")  

        elif hour>=9 and hour<10 and d==('Friday'):
            speak("Biology period")

        elif hour>=10 and hour<11 and d==('Friday'):
            speak("History period")

        elif hour>=11 and hour<12 and d==('Friday'):
            speak("Gk or Ls period")
            
        elif hour>=12 and hour<13 and d==('Friday'):
            speak("Maths period")
            
        elif hour>=13 and hour<15 and d==('Friday'):
            speak("Group A period")
            
        else:
            speak("No period now")
            


            
