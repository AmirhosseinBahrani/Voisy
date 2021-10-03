import speech_recognition as sr
r = sr.Recognizer()

file_audio = sr.AudioFile('NewRecording27.wav')
with file_audio as source:
   audio_text = r.record(source)

print(r.recognize_google(audio_text))