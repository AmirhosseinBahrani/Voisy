import vosk
import sys
import os
import wave
import subprocess
import srt
import json
import datetime

class VoiceRecognizer(object):

    def __init__(self ,filename , WORDS_IN_LINE, sample_rate=16000) -> None:
        super().__init__()
        self.filename = filename
        self.WORDS_IN_LINE = WORDS_IN_LINE
        self.sample_rate=sample_rate

    def CheckInputs(self):
        if not os.path.exists("model"):
            return "can't find model"
        elif os.path.exists(self.filename):
            return "Can't locate file directory"
        elif self.WORDS_IN_LINE < 5:
            return "number of words in line can't be lower than 6"
        

    def Transcribe(self) -> list:
        self.CheckInputs()
        model = vosk.Model("model")
        rec = vosk.KaldiRecognizer(model, self.sample_rate)
        rec.SetWords(True)
        process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i', self.filename, '-ar', str(self.sample_rate) , '-ac', '1', '-f', 's16le', '-'], stdout=subprocess.PIPE)
        results = []
        subtitles = []
        done = False
        while not done:
            data = process.stdout.read(4000)
            if len(data) == 0:
                done = True
                break
            if rec.AcceptWaveform(data):
                results.append(rec.Result())
        results.append(rec.FinalResult())
        
        for i, res in enumerate(results):
            json_data = json.loads(res)
            if not 'result' in json_data:
                continue
            else:
                words = json_data['result']
                for j in range(0, len(words), self.WORDS_IN_LINE):
                    line = words[j : j + self.WORDS_IN_LINE] 
                    subtitles.append(srt.Subtitle(index=len(subtitles), 
                            content=" ".join([l['word'] for l in line]),
                            start=datetime.timedelta(seconds=line[0]['start']), 
                            end=datetime.timedelta(seconds=line[len(line) - 1]['end'])))
        return subtitles

    def CreateSubtitle(self):
        srt_filename = self.filename[0:-4]
        f = open(srt_filename + ".srt", "x")
        f.write(srt.compose(rec.Transcribe()))
        f.close()

    def GenerateSubtitle(self):
        subtitle = self.Transcribe()
        self.CreateSubtitle()
        
    def PutSubtitleInVideo(self):
        srt_filename = self.filename[0:-4]
        generator = lambda txt: TextClip(txt, font='Arial', fontsize=16, color='white')
        subtitles = SubtitlesClip(srt_filename + ".srt", generator)
        video = VideoFileClip(srt_filename + ".mp4")
        result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])
        result.write_videofile(srt_filename + "(Subtitle)" + ".mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")



if __name__ == "__main__":
    filename = "sa" #without file format
    rec = VoiceRecognizer(filename + ".mp3",7)
    rec.GenerateSubtitle()
