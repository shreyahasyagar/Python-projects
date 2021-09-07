import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'baymax' in command:
                command = command.replace('baymax', '')
                print(command)
    except:
        pass
    return command


def run_baymax():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'who are you' in command:
        talk('Hi, I am Baymax. Your personal voice assistant')
    elif 'are you there' in command:
        talk('Always for your service')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('sorry, i did not quite get that. please repeat')


while True:
    run_baymax()