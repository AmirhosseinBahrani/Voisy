import speech_recognition as sr
import time
r = sr.Recognizer()

file_audio = sr.AudioFile('saa.wav')
time_to_start = 0



while True:
   start = time.time()
   with file_audio as source:
      
      try:
         audio_text = r.listen(file_audio,0.7)

         print(r.recognize_google(audio_text))
      except sr.WaitTimeoutError:
         end = time.time()
         time_to_start = start - end
         print()
         #should remove time that sr recognize
   
      


print(r.recognize_google(audio_text))