from pydub import AudioSegment

class Convertor: 
    def convertToMp3(self , name , formatOfFile="wav" , address=None):
        if address == None :
            address = ".\\audio\\others\\" + name + "." + formatOfFile
        src = (".\\audio\\mp3\\" + name + ".mp3")
        audio = AudioSegment.from_file(address)
        audio.export(src , format="wav") 