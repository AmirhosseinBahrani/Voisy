import sounddevice as sd 
from scipy.io.wavfile import write 
import os 

class Record:
    def record(self , name , duration):
        freq = 48000
        address = ".\\audio\\records\\" + name + ".mp3"
        recording = sd.rec(int(duration * freq), samplerate=freq ,channels=2) 
        sd.wait() 
        open(address , "x")
        write(address , freq , recording)
