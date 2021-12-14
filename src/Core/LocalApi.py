from flask import Flask, render_template
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
import shutil
app = Flask(__name__)

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


    def CreateSubtitle(self, transcribtedText): 
        srt_filename = self.filename[0:-4]
        f = open(srt_filename + ".srt", "x")
        f.write(srt.compose(transcribtedText))
        f.close()

    def GenerateSubtitle(self):
        transcribtedText = self.Transcribe()
        self.CreateSubtitle(transcribtedText)
        print("Done")


@app.route('/vr/<filename>')
def my_link(filename):
    print(filename)
    # get real file name
    newfilename = ""
    for i in filename:
        if i == "-":
            newfilename += "/"
        else :
            newfilename += i
    
    # copy file to new path for recognizing
    new_path = shutil.copy2(newfilename, "./audio/mp3")

    new_filename = "." + new_path[1:len(new_path)]
    print(new_filename)
    rec = VoiceRecognizer(new_filename , 7)
    rec.GenerateSubtitle()
    return new_path


if __name__ == '__main__':
  app.run(debug=True)
