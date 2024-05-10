#!/usr/bin/env python
# coding: utf-8

# In[1]:

#from YT_auto import music

#from News import *
import randfacts
from pyjokes import *
#from weather import *
import datetime
#from search import sear
import random2
import math
import warnings
#import open
import os
import serial
import time

from selenium import webdriver

class infow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.blackbox.ai/")
        search_input = self.driver.find_element("xpath", '//*[@id="chat-input-box"]')

        search_input.click()
        search_input.send_keys(query)
        enter=self.driver.find_element("xpath",'/html/body/div[2]/main/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[3]/button')
        enter.click()
    


    
from selenium import webdriver

class infow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.blackbox.ai/")
        search_input = self.driver.find_element("xpath", '//*[@id="chat-input-box"]')

        search_input.click()
        search_input.send_keys(query)
        enter=self.driver.find_element("xpath",'/html/body/div[2]/main/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[3]/button')
        enter.click()
        
def quitApp():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 18:
        print("have a good day sir")
        speak("have a good day sir")
    else:
        print("Goodnight sir")
        speak("Goodnight sir")
    print("Offline")
    exit(0)
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return ("Morning")
    elif hour >= 12 and hour < 16:
        return ("Afternoon")
    elif hour >= 16 and hour < 19:
        return ("evening")
    else:
        return ("night")
    
    
import pyttsx3 as p
import speech_recognition as sr
engine =p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',140)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):

    engine.say(text)
    engine.runAndWait()
today_date = datetime.datetime.now()
r=sr.Recognizer()
speak("Tell the wake up word")
wake = "hello Nova"
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening")
    audio = r.listen(source)
    wakeword = r.recognize_google(audio)

    print(wakeword)
if wake == wakeword:
    while True:
        speak("hello sir, good " + wishme() + ", i'm here to assist you.")
        speak("How are you")
        break
               
    


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "and" "about" and "you" in text:
    speak("iam having a good day sir")
    speak("what can i do for you")
while True:
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio=r.listen(source)
        text2=r.recognize_google(audio)

    if "information" in text2:
        speak("you need information related to which topic?")

        with sr.Microphone() as source:
            r.energy_threshold=10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening...")
            audio=r.listen(source)
            infor=r.recognize_google(audio)


            info_instance = infow()
            info_instance.get_info(infor)

    elif "play" and "video" in text2:
        speak("you want me to play which video??")
        with sr.Microphone() as source:
            r.energy_threshold=10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening...")
            audio=r.listen(source)
            vid=r.recognize_google(audio)
            assist = music()
            assist.play()


    elif "funny" and "joke" in text2:
        speak("Get ready for some chuckles")
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)
    elif "your name" in text2:
        speak("My name is YOYO")
    elif "fact" in text2:
        speak("Sure sir , ")
        x = randfacts.getFact()
        speak("Did you know that," + x)
        print(x)
    elif "game" in text2:
        speak("enter your lower limit sir")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening.....')
            audio = r.listen(source)
            lower = int(r.recognize_google(audio))
        speak("now, Enter your upper limit")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening.....')
            audio = r.listen(source)
            upper = int(r.recognize_google(audio))
        x = random2.randint(lower, upper)
        speak("\n\tYou've only " + str(round(math.log(upper - lower + 1, 2))) + "chances to guess the integer!\n")
        print("\n\tYou've only " + str(round(math.log(upper - lower + 1, 2))) + "chances to guess the integer!\n" + str(upper), str(lower))
        count = 0
        while count < math.log(upper - lower + 1, 2):
            count += 1
            speak("start guessing")
            speak("Guess a number")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print('Listening.....')
                audio = r.listen(source)
                guess = int(r.recognize_google(audio))
            if x == guess:
                print("Congratulations you did it in " + str(count) + " try")
                speak("Congratulations you did it in " + str(count) + " try")
                break
            elif x > guess:
                print("You guessed too small!")
                speak("You guessed too small!")
            elif x < guess:
                print("You Guessed too high!")
                speak("You Guessed too high!")
        if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            speak("\nThe number is %d" % x)
            print("\tBetter Luck Next time!")
            speak("\tBetter Luck Next time!")

    #(elif "reboot the system" in text2:
        speak("Do you wish to restart your computer ?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening.....')
            audio = r.listen(source)
            restart = r.recognize_google(audio)
    elif "light off" in text2:
        #if Light_status_flag == True:
        cmd = "OFF"
        Status = write_read(cmd)
        speak("Lights are turned off")
        #elif Light_status_flag == False:
    elif "stop" or "exit" or "end" in text2:
         speak("It's a pleasure helping you and I am always here to help you out!")
         quitApp()


        


# In[ ]:




