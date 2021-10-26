import sounddevice as sd 
from scipy.io.wavfile import write 

def record(name , duration):
    freq = 48000
    duration = 10
    recording = sd.rec(int(duration * freq), samplerate=freq ,channels=2) 
    sd.wait() 
    write(".\\audio\\wav\\MyRecording.wav", freq, recording) 
    print(recording)
record("ali" , 5)