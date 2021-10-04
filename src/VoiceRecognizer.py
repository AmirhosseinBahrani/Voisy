import speech_recognition as sr
import time
r = sr.Recognizer()
def listen():
   with sr.Microphone() as sound:
      print("speak")
      audio = r.listen(sound)
      return audio
a = listen()
print(a)