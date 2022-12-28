from http import server
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys, pyjokes
import pyautogui
from time import *

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
volume =engine.getProperty('volume')
engine.setProperty('volume',5.0)
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',150)
#text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert voic into text
def takecommand():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=100,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        #speak("say that again")
        return "none"
    query= query.lower()
    return query




def sendEmail(to,content):
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("bagdevaibhav551@gmail.com","#Bagdevaibhav551")
    server.sendmail("bagdevaibhav551@gmail.com",to,content)
    server.close()

def wish():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak(hour)
    speak("I am Ms. Anna boss. please tell me how may i help you")
    

def Pass(pass_inp):
    password = "ok"
    passw =str(password)

    if passw==str(pass_inp):
        speak("Access Granted")

        import anna

    else:
        speak("Access not Granted")

if __name__ == "__main__":
    speak("This Particular file is Password Protected")
    speak("Kindly Provide the Password to Access")
    passs = takecommand()

    Pass(passs)

    
def TaskExecution():
    wish()
    while True:
    #if 1:
        query = takecommand().lower()


        if "open notepad" in query:
            npath=r"C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif"close notepad" in query:
            speak("ok Boss, closing notepad")
            os.system("taskkill /f /im notepad.exe")

    
        elif "open cmd" in query:
            os.system("Start cmd")

        elif"close cmd" in query:
            speak("ok Boss, closing cmd")
            os.system("taskkill /f /im cmd.exe")

        elif"open camera" in query:
            cap = cv2.VideoCapture(1)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif"play music" in query:
            music_dir =r"E:\\music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                     os.startfile(os.path.join(music_dir,song))

        elif'what is my ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Youre Ip address is {ip}")
        
        elif 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(result)
            print(result)

        elif"open youtube" in query:
            """speak("Boss, what should i search on youtube")
            su= takecommand().lower()
            webbrowser.open(f"{su}")"""
            speak("ok Boss, opening Youtube")
            webbrowser.open("www.youtube.com")

        elif"open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("ok Boss, opening Facebook")

        elif"close facebook" in query:
            speak("ok Boss, closing facebook")
            os.system("taskkill /f /im https://www.facebook.com/")
        
        elif"open instagram" in query:
            webbrowser.open("www.instagram.com")
            speak("ok Boss, opening Instagram")

        elif"open google" in query:
            speak("Boss, what should i search on google")
            cm= takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "resso" in query:
            webbrowser.open("www.resso.com")
        
        elif"send message"in query:
            kit.sendwhatmsg("+9190112593341","this is example not  MESSage",10,47)

        elif"play song on youtube" in query:
            speak("which song plays on YouTube")
            rm= takecommand().lower()
            kit.playonyt(f"{rm}")

        elif"email to vaibhav" in query:
            try:
                speak("wha should i say")
                content = takecommand().lower()
                to ="vaibhavb9204@gmail.com"
                sendEmail(to,content)
                speak("Email has been send to vaibhav")
            
            except Exception as e:
                print(e)
                speak("sorry Boss, i am not able to send this mail to vaibhav")

        #elif"Ajay" in query:
         #   speak(" Bhushan is nibba ,BHushan is the son of vaibhav. he is chaka boy.")
          #  speak(" for more information, ask to vaibhav and arshad, adinath")
    

        elif"who are you" in query:
            speak("I am Anna, yours assistent boss")

        elif"thanks" in query:
            speak("Most welcome boss")

        elif"love you" in query:
            speak("hummmm, your so naughty boss, Love  you  to  boss <3")

        elif"ok anna" in query:
            speak("Yes Bosss")

        elif"sleep" in query:
            speak("Okay boss, i am going to sleep you can call me anytime ")
            break;

        elif"close notepad" in query:
            speak("ok Boss, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif"set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            speak("alarm set successfully boss")
            if nn==11:
                music_dir =r"E:\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,song[0]))

        elif"tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif"shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif"restart the system" in query:
            os.system("shutdown /s /t 5")

        #elif"mode on":
        #    os.system("rundll32.exe powrprof.dll.SetSuspendState 0,1,0")


        elif"switch the window" in query:
            pyautogui.keyDown("alt")
            time.sleep(2)
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif"where i am" in query or "where we are" in query:
            speak("wait boss, let me check")

            #try:
               # ipAdd = request.get('https://api.ipify.org').text
                #print (ipAdd)

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            speak("ok, bye boss have a good day")
            sys.exit()
