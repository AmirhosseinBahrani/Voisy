import speech_recognition as sr
import time
from FileResizer import FileResizer
import math
from pydub import AudioSegment
import speech_recognition as sr
import time

r = sr.Recognizer()

def recognize(audio_text):
   return r.recognize_google(audio_text)
      
r = sr.Recognizer()
file_audio = sr.AudioFile('/src/saq.wav')
time_to_start = 0
first_start = time.time()

while True:
   start = time.time()
   try:
      #r.adjust_for_ambient_noise(source)
      with file_audio as source:
         audio_text = r.listen(source,0.7)
         recognize(audio_text)
         #print(r.recognize_google(audio_text, language="en-US", show_all=False))
   except sr.WaitTimeoutError:
      end = time.time()
      time_to_start = abs(start - end) * 100
      print(abs(time_to_start * 100))
      t1 = time_to_start * 1000 #Works in milliseconds
      FR = FileResizer("saq.wav",t1).extract()
      FR.extract()
      # Update Audio file
      file_audio = sr.AudioFile('saq.wav')