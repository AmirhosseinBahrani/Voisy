import vosk
import sys
import os
import wave
import subprocess
import srt
import json
import datetime
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

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
        print(srt_filename)
        import re

        with open(srt_filename + '.srt', 'r') as h:
            sub = h.readlines()
        re_pattern = r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} -->'
        regex = re.compile(re_pattern)
        # Get start times
        start_times = list(filter(regex.search, sub))
        start_times = [time.split(' ')[0] for time in start_times]
        # Get lines
        lines = [[]]
        for sentence in sub:
            if re.match(re_pattern, sentence):
                lines[-1].pop()
                lines.append([])
            else:
                lines[-1].append(sentence)
        lines = lines[1:]         
        subs = {}
        for i,j in zip(start_times,lines):
            subs[i] = j


        import cv2
        import pandas as pd
        from moviepy.editor import VideoFileClip

        def pipeline(frame):
            try:
                cv2.putText(frame, str(next(dfi)[1].sentence), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA, True)
            except StopIteration:
                pass
            # additional frame manipulation
            return frame
        print(subs)
        dfi = subs.items()
        video = VideoFileClip(srt_filename + ".mp4")
        out_video = video.fl_image(pipeline)
        out_video.write_videofile("vidout.mp4", audio=True)




if __name__ == "__main__":
    filename = "audio/mp3/qe" #without file format
    rec = VoiceRecognizer(filename + ".mp3",7)
    #rec.GenerateSubtitle()
    rec.PutSubtitleInVideo()