import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
#import vlc
import urllib
import urllib3
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import random   
from time import strftime
import pyttsx3
import datetime

# for converting text to speech
engine = pyttsx3.init()

rate = engine.getProperty('rate')
#print(rate)
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
#print(volume)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print("Lisa: "+ audio)
    engine.say(audio)
    engine.runAndWait()

# for interpreting user's voice
def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print("You said",command,"\n")
        except sr.UnknownValueError:
            print("Processing could not be done!!!")
        except sr.RequestError:
            print("Connection could not be established")
        return command

if __name__ == "__main__":
    while True:

        query = mycommand()
        query = query.lower()

        if 'open reddit' in query:
            reg_ex = re.search('open redit (.*)', query)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(2)
                url = url + 'search/?q=' + subreddit
            webbrowser.open(url)
            speak("The Reddit content has been opened for you sir.")        

        elif 'shutdown' in query:
            speak('Bye bye sir. Have a nice day.')
            sys.exit()

        # open website
        elif 'open' in query:
            reg_ex = re.search('open (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                speak("The website you have requested has been opened for you sir.")
            else:
                pass

        #greetings
        elif 'hello' in query:
           time = int(datetime.datetime.now().hour)
           if time >= 0 and time < 12:
               speak("Hello sir. Good morning.")
           elif time >= 12 and time <= 17:
                speak("Hello sir. Good afternoon.")
           elif time >= 17 and time < 0:
               speak("Hello sir. Good evening.")
        
        elif 'help me' in query:
            speak("""
            You can use these commands and I'll help you out:
            1. Open reddit subreddit : Opens the subreddit in default browser.
            2. Open xyz.com : opens xyz website in default browser
            3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
            4. Current weather in {cityname} : Tells you the current condition and temperture
            5. Hello
            6. play me a video : Plays song in your VLC media player
            7. change wallpaper : Change desktop wallpaper
            8. news for today : reads top news of today
            9. time : Current system time
            10. top stories from google news (RSS feeds)
            11. tell me about xyz : tells you about xyz
            """)
            
        # joke
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers = {"Accept":"application/json"})            
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))            
            else:
                speak("Oops! I ran out of jokes")

        # top stories from google news
        elif 'news for today' in query:
            try:
                news_url = "https://news.google.com/news/rss"
                client = urlopen(news_url)
                xml_page = client.read()
                client.close()
                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item")            
                for news in news_list[:15]:
                    speak(news.title.text.encode('utf-8'))
            except Exception as e:
                print(e)

