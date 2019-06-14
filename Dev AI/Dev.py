import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    #This function helps to speak whatever is passed in a string through parameter
    engine.say(audio)                            
    engine.runAndWait()

def greet():
    #This function greets the user according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am PIE. How may i help you")

def takeCommand():
    #Gets all the microphone available and select we want

    #mic_list = sr.Microphone.list_microphone_names() 
    #print(mic_list)

    #listen and recognize the speach using speach recognizition

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #recognizer_instance.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: " ,query)

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
        
    return query

def sendEmail(to, content):
    #send email through simple mail transfer protocol
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Email', 'Password')
    server.sendmail('Email', to, content)
    server.close()


if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Give me 2 minutes...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'on youtube' in query:
            webbrowser.open('www.youtube.com/results?search_query='+query)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is" + strTime)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Suhag Sapra\\Desktop\\SLAM\\csgo'
            songs = os.listdir(music_dir)
            length_of_songs = len(songs)
            print(songs)    
            random_num = random.randint(0,length_of_songs)
            os.startfile(os.path.join(music_dir, songs[random_num]))

        elif 'send email' in query:
            try:
                receivers = {'abc': 'Email'}
                speak("Okay. Tell me the email address")
                to = takeCommand().lower()
                print(receivers[to])
                speak("What should I say?")
                content = takeCommand()  
                sendEmail(receivers[to], content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("Sorry! i am Unable to send email")

        else:
            webbrowser.open("www.google.com/search?q="+query)

