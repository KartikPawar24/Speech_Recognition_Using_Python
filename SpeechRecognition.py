import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import random

engine = pyttsx3.init()

male_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

engine.setProperty('voice', male_voice)

def speak(audio):
    print("David: "+ audio)
    engine.say(audio)
    engine.runAndWait()
speak("Hello Kartik, i'm your new digital personal assistant and my name is David")

def greetme():
    globals()['time'] = int(datetime.datetime.now().hour)
    if time >=0 and time < 12:
        speak("Good Moring Kartik!!!")
    if time >= 12 and time < 17:
        speak("Good afternoon Kartik!!!")
    if time >= 17 and time < 24:
        speak("Good evening Kartik!!!")

    Time = datetime.datetime.now()
    speak(Time.strftime("Now the time is: %H : %M Indian Standard Time Hours"))
    globals()['Today'] = datetime.date.today()
    speak(Today.strftime("Today is: %A, %d %B, %Y"))
greetme()


def tasks():
    speak("Here are the list of some tasks that you can give me that i can perform it")
    speak("Say 'Open Youtube'")
    speak("Say 'Open Google'")
    speak("Say 'Play Random Game'")
    speak("Say 'Perform Search Operation'")
    speak("Say 'What can you do'")
    speak("Say 'who created you'")
    speak("Say 'In which language are you written'")
    speak("Say 'what is the time'")
    speak("say 'what is the date'")
    speak("Say 'Open Chrome'")
    speak("Say 'Search in Google'")
    speak("Say 'Shut Down' or 'Exit' or 'Stop'")
    speak("How may i help you?")

tasks()

def mycommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print("User: "+query+"\n")
        except sr.UnknownValueError:
            speak("I didn't understood what you spoke")
        except sr.RequestError:
            speak("Please check your connectivity like internet connection")
        return query

if __name__ == "__main__":
    while True:

        query = mycommand()
        query = query.lower()

        if "open youtube" in query:
            speak("Opening youtube hang there!")
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("Opening Google Search Engine")
            webbrowser.open("www.google.com")


        elif "how are you" in query:
            str = ["I'm fine", "Nice", "Fine", "I'm waiting to work with you Kartik", "I'm full of energy"]
            speak(random.choice(str))

        elif "play random game" in query:
            speak("Ok, Kartik let us play a game called 'Guessing the random number'")
            speak("Enter the range of the number for which a random number is to be generated:")
            ran_num = int(input("Enter the range of the random number: "))
            speak("Your random number range is: {}".format(ran_num))
            random_number = random.randint(1, ran_num)
            count = 0
            bool = True
            while bool:
                guessed_number = int(input("Enter the guessed random number: "))
                count = count + 1
                if random_number == guessed_number:
                    speak("You have guessed it correctly")
                    print("You guessed it correctly at {} attempt".format(count))
                    bool = False
                else:
                    speak("You guessed wrong number, please try another number")

        elif "perform search operation" in query:
            speak("what should i actually search for on wikipedia Kartik, please type your search:")
            Search = input("What should i actually search for: ")
            speak("I found something like this on Wikipedia as:")
            result = wikipedia.summary(Search, sentences = 4)
            speak(result)
            speak("Search Operation completed Kartik")

        elif "search in google" in query:
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome %s"
            url = "https://www.google.com/#q="
            speak("Enter what you want to search in Google Search:")
            search_item = input()
            speak("These are the results i have found on Google Chrome Kartik\n")
            webbrowser.get(browser_path).open(url+search_item)

        elif "what can you do" in query:
            tasks()

        elif "who created you" in query:
            speak("My creator's name is: Kartik Pawar")

        elif "in which language are you written" in query:
            speak("Kartik wrote me in pure 'Python Programming Language'")
            speak("And he is upgrading my new abilities to perform more tasks and to interact with humans")

        elif "what is the time" in query:
            ti_me = datetime.datetime.now()
            ti_me = ti_me.strftime("Now the time is: %H : %M Indian Standard Time Hours")
            speak(ti_me)

        elif "what is the date" in query:
            speak(Today.strftime("Today is: %A, %d %B, %Y"))

        elif "open chrome" in query:
            path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            speak("Opening Google chrome")
            os.startfile(path)

        elif "shut down" or "exit" or "stop"  in query:
            speak("Bye Kartik and remember i am there for your help!!!")
            speak("Thank you for making me the part of your today's activity!!!")
            if time >= 22:
                speak("Are you going to sleep?")
                ans = input("Enter y or n:\n")
                if ans.lower() == "y":
                    speak("Good night Kartik!!!")
            speak("David is shutting down!!!")
            sys.exit()
