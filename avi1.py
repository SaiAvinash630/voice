import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia  
import webbrowser
import os
import smtplib # Python library for sending emails using the Simple Mail Transfer Protocol (SMTP)
import random
import pywhatkit as wt
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 0.5
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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saiavinash9393@gmail.com', 'Sai9393Avinash')
    server.sendmail('sai9393avinash@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\avinash'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("To whom")
                t = takeCommand()
                l = t.replace(" ", "")
                u = l.lower()
                to = u+"@gmail.com"
                speak("What should I say?")
                content = takeCommand()
                # to = "praneethsai800@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        elif 'send whatsapp message' in query:
            try:
                while(1):
                    speak("To whom: ")
                    co= takeCommand()
                    if 'sahi' in query:
                        w='+918008515517'
                        speak("what is the message:")
                        m=takeCommand()
                        wt.sendwhatmsg_instantly(w,m)
                        print("Message has been sent")
                        speak("Message has been sent")
                        break
                    else:
                        c=co.replace(" ","")
                        if len(c)==10:
                            w="+91"+c
                            speak("what is the message: ")
                            m= takeCommand()
                    # now = datetime.datetime.now()
                            wt.sendwhatmsg_instantly(w,m)
                            print("Message has been sent")
                            speak("Message has been sent")
                            break
                        else:
                            speak("number is not correct message cant be sent, say the number again")
                    



            except Exception as e:
                print(e)
                speak("Sorry unable to send")
            # wt.sendwhatmsg("+916305847139","hello")
            # try:
                # speak("what should i send?")
                # content=takeCommand()
                # to=8008515517
                # sendmessage(to,content)
                # speak("message has been sent!")
                # print("message has been sent!")
        
               
        elif 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go to hell' in query or 'hold on' in query or 'exit' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))
            
            break          
