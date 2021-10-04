import speech_recognition as sr
from pydub import AudioSegment
def convertToWav(name):
    address = "./" + name + ".wav"
    src = (r"./" + name + ".mp3")
    audio = AudioSegment.from_mp3(src)
    audio.export(address , format="wav")