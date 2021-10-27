import sounddevice as sd 
from scipy.io.wavfile import write 
import os

def record(name , duration):
    freq = 48000
    address = ".\\audio\\wav\\" + name + ".wav"
    recording = sd.rec(int(duration * freq), samplerate=freq ,channels=2) 
    sd.wait() 
    write(address , freq , recording)
