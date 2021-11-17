from pydub import AudioSegment
import ffmpeg


class FileResizer:
    def __init__(self, file_name, start_time, end_time):
        self.file_name = file_name
        self.start_time = start_time
        self.end_time = end_time
        
    def get_lenth():
        return ffmpeg.probe(str(self.file_name))['format']['duration']

    def extract():
        t1 = self.start_time * 1000 #Works in milliseconds
        t2 = self.get_lenth()
        newAudio = AudioSegment.from_wav(str(self.file_name))
        newAudio = newAudio[t1:t2]
        newAudio.export(str(self.file_name), format="wav")
