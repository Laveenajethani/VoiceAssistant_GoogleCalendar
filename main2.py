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

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception: ",str(e))
	return said

test = get_audio()
if "hello" in test:
	speak("hello,how are you?")

if "what is your name" in test:
	speak("my name is laveena")