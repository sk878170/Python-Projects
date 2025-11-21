import speech_recognition as sr 
from selenium import webdriver

class voice:
    def __init__(self):
        self.recognizer=sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source) # Listen for the user's
                    command= self.recognizer.recognize_google(audio)
                    print(command)

                    if "search" in command:
                        driver=webdriver.Edge()
                        driver.get(f"https://www.google.com/search?q={command.split('search')[-1]}")

            except sr.UnknownValueError:
                print("Could not understand audio")
                pass

listener=voice()

                

            
