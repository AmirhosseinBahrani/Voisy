from pydub import AudioSegment
def convertToWav(name):
    address = ".\\audio\\wav\\" + name + ".wav"
    src = (".\\audio\\mp3\\" + name + ".mp3")
    audio = AudioSegment.from_mp3(src)
    audio.export(address , format="wav")
 
