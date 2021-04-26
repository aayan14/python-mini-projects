import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def wishMe():
    hours = int(datetime.datetime.now().hour)
    if hours > 0 and hours < 12:
        speak('Good Morning')
    elif hours > 12 and hours < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('I am Jarvis. How may I help you')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # takes microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
    except Exception as e:
        print(e)
        speak('Sorry. Please say that again')
        return 'None'
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aayansingh806@gmail.com', '1432000A')
    server.sendmail('aayansingh806@gmail.com', to, content)
    server.close()


def calculation(first, second, operation):
    try:
        if (operation == 'addition'):
            return first + second

        elif (operation == 'subtraction'):
            return first - second

        elif (operation == 'multiplication'):
            return first * second

        elif (operation == 'division'):
            return first / second

        elif (operation == 'modulus'):
            return first % second

    except Exception as e:
        print(e)
        return 'Sorry!! Please try again.'


def tellQuote():
    try:
        page = str(random.randint(1, 48))
        url = 'http://www.values.com/inspirational-quotes?page='+page

        r = requests.get(url)
        htmlcontent = r.content

        soup = BeautifulSoup(htmlcontent, 'html.parser')
        quotes = []
        table = soup.find('div', attrs={'id': 'all_quotes'})
        for item in table.findAll('div', attrs={'class': "col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"}):
            quotes.append(item.img['alt'].split(' #')[0])

        return random.choice(quotes)
    except Exception as e:
        print(e)
        return 'Sorry. An error occured. Please try again'


if __name__ == '__main__':
    wishMe()
    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)
            break

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            break

        elif 'open google' in query:
            webbrowser.open('google.com')
            break

        elif 'open V T U website' in query:
            webbrowser.open('vtu.ac.in')
            break

        elif 'open B M S I T website' in query:
            webbrowser.open('bmsit.ac.in')
            break

        elif 'the current time' in query:
            currtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(currtime)
            break

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break

        elif 'open Spotify' in query:
            spotifyPath = "C:\\Users\\HP\\AppData\\Roaming\\Spotify\\Spotify.exe"
            try:
                os.startfile(spotifyPath)
            except Exception as e:
                print(e)

        elif 'email to' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'aayansingh806@gmail.com'
                sendEmail(to, content)
                speak('The email has been sent.')
            except Exception as e:
                print(e)
                speak('An error occured while sending the email. Please try again.')
            break

        elif 'do a calculation' in query:
            try:
                speak('What is the first no.?')
                a = int(takeCommand())
                print(f'First number is {a}')
                speak('What is the second number?')
                b = int(takeCommand())
                print(f'Second number is {b}')
                print('Operation List: Addition, Subtraction, Multiplication, Division')
                speak('What operation do you want to perform')
                op = takeCommand()
                answer = calculation(a, b, op)
                speak(f'The result is {answer}')
            except Exception as e:
                print(e)
                speak('An error occured.')
            break

        elif 'tell me a quote' in query:
            quote = tellQuote()
            print(quote)
            speak(quote)

        elif 'stop' in query:
            exit()
