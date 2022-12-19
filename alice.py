# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:11:51 2022

@author: user
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup
import PyPDF2
listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
       engine.say(text)
       engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alice' in command:
                command=command.replace('alice', '')
                print(command)
    except:
      pass        
    return(command) 
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
         song=command.replace('play','')
         talk('playing '+ song)
         pywhatkit.playonyt(song)       
    elif 'time' in command:
         time=datetime.datetime.now().strftime('%H:%M')
         print(time)
         talk('Current time is '+ time)
    elif 'who is'in command:
        person=command.replace('Who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
          talk('Sorry, i have a headache')
    elif 'are you single' in command:
        talk('Yes i am but not interested in dating you!')
    elif 'joke' in command:
       talk(pyjokes.get_joke())
    elif 'good morning' in command:
        talk('Good morning')
    elif 'good afternoon' in command:
        talk('Good afternoon')
    elif 'good evening' in command:
        talk('Good evening')
    elif 'good night' in command:
        talk('Good night')
    elif 'bye' in command:
        talk('bye')
        exit(0)
    elif 'remind me ' in command:
        remmebermsg=command.replace('remind me','')
        remmebermsg=remmebermsg.replace('alice', '')
        talk("you Told me :"+remmebermsg)
        remember=open('data.txt','w')
        remember.write(remmebermsg)
        remember.close()
    elif 'what do you remember' in command:
       remember=open('data.txt','r')
       talk("You told me that"+remember.read())
    elif  'good job' in command:
         talk('I will always be at your service')
         exit(0)
    elif 'google search'in command:
         import wikipedia as googleScrap
         command=command.replace('alice','')
         command=command.replace("google search",'')
         command=command.replace('google','')
         talk('this what i have found on the web')
         pywhatkit.search(command)
         
         try:
              result= googleScrap.summary(command,2)
              print(result)
              talk(result)
         except:
             talk('no speak able data available!')
    elif 'temperature' in command:
        
        search='temperature in mangalore'
        url=f'https://www.google.com/search?q={search}'
        r=requests.get(url)
        data=BeautifulSoup(r.text,'html.parser')
        temp=data.find('div',class_='BNeawe').text
        talk(f'current {search} is {temp}')
    elif 'read' in command:
        engine.say('Let me read it for you!')
        book=open('Ds pdf.pdf','rb')
        pdfReader=PyPDF2.PdfFileReader(book)
        pages=pdfReader.numPages
        print(pages)
        for num in range(1,pages):
          page=pdfReader.getPage(1)
          text=page.extractText()
          engine.say(text)
          engine.runAndWait()
    else:
        talk('Please say the command again')

    
   
  
while True:
    run_alexa()