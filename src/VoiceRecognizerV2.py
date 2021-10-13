import speech_recognition as sr
import time
r = sr.Recognizer()
def recognize(source):
   return r.recognize_google(audio_text)
def fileToText(name):
   audioFile = sr.audioFile(r + "./" + "wav")
   with audioFile as sound:
      text = r.record(sound)
   return text
def listen():
   with sr.Microphone() as sound:
      print("speak")
      audio = r.listen(sound)
      return audio
a = listen()
print(a)
