import os
import playsound
from gtts import gTTS 
import time
import speech_recognition as sr 

def speak(text):
	tts = gTTS(text=text,lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

speak("hello laveena kya hal chal")