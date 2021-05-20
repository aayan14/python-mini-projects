# -------------------------------------- PROJECT TOPIC: DESKTOP VOICE ASSISTANT ---------------------------------------

'''Description : Desktop voice assistant is an application made using python programming languages speech recognition 
module and other useful modules which listen to the user and try to recognize its speech and convert it to an string. 
Based on the command, it performs diffrent action and automates some works which user does manually. Some of the action 
it performs are like opening a website, checking the time, getting the current news, wikipedia search etc.'''

#----------------------------------------------------CODE-------------------------------------------------------------#

# Importing the useful dependencies required for the project
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests
from bs4 import BeautifulSoup
from gnewsclient import gnewsclient

# Create a pyttsx3 instance and use SAPI5 which is a Microsoft's API for speech recognition
engine = pyttsx3.init('sapi5')
# Voices is a list of 2 voices (male an female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice required

# Wishes the user according to time


def wishMe():
    hours = int(datetime.datetime.now().hour)  # Check the time (hours)
    if hours > 0 and hours < 12:
        speak('Good Morning Sir')
    elif hours > 12 and hours < 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')

    speak('I am Desktop Voice Assistant. How may I help you')

# speak function takes string parameter and outputs it as an audio
# and wait for the command


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# takeCommand function listens to the audio input by the user and coverts it to a string to perform operations
def takeCommand():
    # Create a instance of Recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:    # Use microphone as the source of audio input by the user
        print('Listening...')
        # It tell the assistant to wait for 1 second after the user has stopped speaking
        r.pause_threshold = 1
        # Minimum energy required by the user so the assistant hears the command
        r.energy_threshold = 100
        audio = r.listen(source)       # Input is saved in the variable audio

    # Coverting the audio file to string
    try:
        print('Recognizing...')
        # Recognizing the audio file on basis language mentioned and save the string in query variable
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')   # Print what user serializeDate

    # If an error occurs while recognizing
    except Exception as e:
        # print the error message and tell user to try again
        print(e)
        speak('Sorry. Please say that again')
        return 'None'

    # Returns the audio converted to string
    return query

# calculation function is a simple calculator for 2 operands


def calculation(first, second, operation):
    try:
        if (operation == 'addition'):  # Addition
            return first + second

        elif (operation == 'subtraction'):  # Subtraction
            return first - second

        elif (operation == 'multiplication'):  # Multiplication
            return first * second

        elif (operation == 'division'):  # Division
            return first / second

        elif (operation == 'modulus'):  # Modulo
            return first % second

    # If error occurs, tell user to try again
    except Exception as e:
        print(e)
        return 'Sorry!! Please try again.'


# tellQuote is a function which uses WEB SCRAPPING technique to get a random quote from a website
def tellQuote():
    try:
        page = str(random.randint(1, 48))
        url = 'http://www.values.com/inspirational-quotes?page=' + \
            page    # Link to the web page which is to be scrapped

        # Get the HTML content of the page
        r = requests.get(url)
        htmlcontent = r.content

        # Use the html parser to beautify the content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        quotes = []     # An empty list which will contain the quotes from the particular page

        # Finally we extract the tags around which the quotes are wrapped and add it to our empty list
        table = soup.find('div', attrs={'id': 'all_quotes'})
        for item in table.findAll('div', attrs={'class': "col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"}):
            quotes.append(item.img['alt'].split(' #')[0])

        # return a randomly chosen quote from the list
        return random.choice(quotes)

    # If error occurs, tells user to try again
    except Exception as e:
        print(e)
        return 'Sorry. An error occured. Please try again'


# Start of the program
if __name__ == '__main__':

    # Wishes the user
    wishMe()
    while(True):
        # Takes command for user
        query = takeCommand().lower()       # Converts the  audio command to string

        # Performs actions depending on whether the key word is in the query or not

        # Wikipedia search
        if 'wikipedia' in query:      # Checks for the keyword
            speak('Searching...')
            # Edits the query for better searching process
            query = query.replace('wikipedia', '')
            # Gets the result and saves is to a variable
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')

            # Prints and says the result
            print(results)
            speak(results)
            break

        # Opens diffrent website using the WEBBROWSER module in python

        # Checks for the keyword in query
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            break

        elif 'open google' in query:
            webbrowser.open('google.com')
            break

        elif 'open university website' in query:
            webbrowser.open('vtu.ac.in')
            break

        elif 'open college website' in query:
            webbrowser.open('bmsit.ac.in')
            break

        # Checks the query to find the key word
        elif 'the current time' in query:
            # gets the current time using the DATETIME module and formats it to an understandable format
            currtime = datetime.datetime.now().strftime('%H:%M:%S')

            # Prints and says thee current time
            print(currtime)
            speak(currtime)
            break

        # Check for the keyword in query
        elif 'open code' in query:

            # Opens the Visual Studio Code which is present in locally in my device using OS module

            # codePath is the path of the application in my device
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break

        # Check for the keyword in query
        elif 'do a calculation' in query:
            try:
                # Ask for inputs from the user and print them
                speak('What is the first no.?')
                a = int(takeCommand())
                print(f'First number is {a}')
                speak('What is the second number?')
                b = int(takeCommand())
                print(f'Second number is {b}')

                # List the operationd available
                print('Operation List: Addition, Subtraction, Multiplication, Division')
                speak('What operation do you want to perform')
                op = takeCommand()  # Get the operation to be performed
                # Use the calculation function and get the result
                answer = calculation(a, b, op)
                speak(f'The result is {answer}')    # Says the result

            # If error occurs, it asks the user to try again
            except Exception as e:
                print(e)
                speak('An error occured.')
            break

        # Check for the keyword in query
        elif 'tell me a quote' in query:
            # Get a random quote
            quote = tellQuote()
            print(quote)
            speak(quote)
            exit()

        # Ckeck the keyword in query
        elif 'current news' in query:

            # Get Current news using the Google News Client module available in python
            client = gnewsclient.NewsClient(
                language='english', max_results=5)

            # Extract the top 5 news in english language
            for item in client.get_news():

                # Printa and says the title of the news and also mentions the link to the article
                print("Title: " + item['title'])
                speak(item['title'])
                print()
                print("Link: " + item['link'])
                print()
            exit()

        # Ckeck the keyword in query
        elif 'write a note' in query:
            # Creates a text file which will be like a todo list
            speak('What should I write sir')        # Ask what to add
            note = takeCommand()
            file = open('note.txt', 'a')            # Open the file
            speak('Are you sure?')                  # Confirmation
            print('Say YES/NO')
            confirm = takeCommand()
            if confirm == 'yes':
                # If the user has confirmed, create/edit the file with a time stamp
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.writelines('\n' + strTime + ' : ' + note)
                speak('Done.')
                exit()
            exit()

        # Ckeck the keyword in query
        elif 'show notes' in query:
            # Shows the notes/todos
            file = open('note.txt', 'r')
            print(file.read())
            exit()

        # Check for the keyword in query
        elif 'stop' in query:
            # Stops the program
            exit()
