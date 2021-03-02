#J.A.R.V.I.S by JP 
#Youtube Channel Link -: https://tinyurl.com/1smu75d8
#Youtube Channel Name -: Junior Programmer 


#Install Modules 
import pyttsx3 
import speech_recognition
import datetime
import os
import cv2
from requests import get 
import wikipedia 
import webbrowser
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print (audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1 , phrase_time_limit =5)
    try:
        print("Just a moment....")
        query=r.recognize_google(audio , language = 'en-in')
        print (f"You said:{query}")
    except Exception as e :
        speak("Will you please repeat that....")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<=12:
        speak("Good Morning Sir!")
    elif hour>12 and hour<18:
        speak ("Good Afternoon Sir!")
    else :
        speak ("Good Evening!")
    speak ("Hello , i am JARVIS made by Junior Programer. Please tell me how can i help you ?")
 
#To send Email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your Email Address','Your Password')
    server.sendmail('Your email id' , to ,content)
    server.close()


if __name__ == "__main__":
    wish()
    if 1:
        query = takecommand().lower()
#Open Notepad 
        if "open notepad" in query:
            npath = "C:\\Users\\Manisha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"#App Location 
            os.startfile(npath)

#Open OBS Studio
         elif "open command prompt" in query:
             opath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio"
             os.startfile(opath)
             
#Open CMD
        elif "open command prompt" in query:
            cpath = "C:\\Users\\Manisha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools"#App Location
            os.startfile(cpath)

#Open VSC
        elif "open visual studio code" in query:
            vpath = "C:\\Users\\Manisha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code" #App Location
            os.startfile(vpath)

#Open Camera
        elif "open camera" in query :
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.inshow('webcam',img)
                k = cv2.waitKey(50)
                if k== 27:
                    break:
            cap.release()
            cv2.destroyAllWindows()

#Play Music
        elif "play music" in query:
            music_dir = "C:\\Users\\Manisha\\Downloads"
            songs = os.listdir(music_dir)
            os.startfile(os.path,join(music_dir,songs[0]))

#Find IP Address
        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak (f"Your IP address is {ip}")

#Search Wikipedia
        elif "open wikipedia" in query:
            speak ("Searching Wikipedia ....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query , sentance=2)
            speak ("According to Wikipedia")
            speak(results)
            print (results)

#Open Youtube
         elif "Open Youtube" in query:
             speak ("Sir, What should i search on Youtube ?")
             cm=takecommand().lower()
             webbrowser.open(f"{cm}")
             
#Open Facebook
         elif "Open Facebook" in query:
             webbrowser.open("Facebook.com")

#Open Stack Flow
         elif "Open Stackoverflow" in query:
             webbrowser.open("Stackoverflow.com")

#Open Google 
         elif"Open Google" in query:
             speak ("Sir, What should i search on Google ?")
             cm=takecommand().lower()
             webbrowser.open(f"{cm}")

#Open Instagram
         elif "Open Instagram" in query:
             webbrowser.open("instagram.com/tanay_30104")

#Email
         elif "Send Email" is query:
             try:
                 speak("What should i say?")
                 content=takecommand().lower()
                 to = "programmingforjuniors@gmail.com" 
                 sendEmail(to,content)
                 speak ("Email had been send successfully !")

            except Exception as e:
                print (e)
                speak ("Sorry Sir , i am not able to sent this email .")

#Closing Loop 
             elif "No Thanks" in query :
                 speak ("Thanks for using me . Have a good Day!")
                 sys.exit()

             speak ("Sir, Do You have any other work ?")


