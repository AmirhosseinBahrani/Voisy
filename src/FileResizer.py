from pydub import AudioSegment

class FileResizer:
    def __init__(self, files_path, file_name, startMin, startSec, endMin, endSec):
        self.files_path = files_path
        self.file_name = file_name
        self.startMin = startMin
        self.startSec = startSec
        self.endMin = endMin
        self.endSec = endSec

    def extract():
        startTime = startMin*60*1000+startSec*1000
        endTime = endMin*60*1000+endSec*1000
        # Opening file and extracting segment
        song = AudioSegment.from_mp3( files_path+file_name+'.mp3' )
        extract = song[startTime:endTime]
        # Saving
        extract.export( file_name+'.mp3', format="mp3")