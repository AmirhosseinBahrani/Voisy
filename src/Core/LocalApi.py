from flask import Flask, render_template
import sys
import vosk
import os
import wave
import subprocess
import srt
import json
import datetime
import shutil
import uuid
from pydub import AudioSegment
from googletrans import Translator
translator = Translator()


app = Flask(__name__)

class VoiceRecognizer(object):

    def __init__(self ,filename , WORDS_IN_LINE, model_dir,save_file_dir, sample_rate=16000) -> None:
        super().__init__()
        self.filename = filename
        self.WORDS_IN_LINE = WORDS_IN_LINE
        self.sample_rate=sample_rate
        self.ModelDirectory = model_dir
        self.DirForSaving = save_file_dir
        self.uuid = str(uuid.uuid4())

    def CheckInputs(self):
        if not os.path.exists("model"):
            return "can't find model"
        elif os.path.exists(self.filename):
            return "Can't locate file directory"
        elif self.WORDS_IN_LINE < 5:
            return "number of words in line can't be lower than 5"


    def Transcribe(self) -> list:
        self.CheckInputs()
        model = vosk.Model(self.ModelDirectory)
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
                    subtitles.append(
                        srt.Subtitle(index=len(subtitles),
                            content=" ".join([l['word'] for l in line]),
                            start=datetime.timedelta(seconds=line[0]['start']),
                            end=datetime.timedelta(seconds=line[len(line) - 1]['end']))
                            )
        return subtitles


    def CreateSubtitle(self, transcribtedText):
        srt_filename = self.DirForSaving[0:-4]
        print(srt_filename + "(" + self.uuid + ")" + ".srt","srtfile")
        f = open(srt_filename + "(" + self.uuid + ")" + ".srt", "w")
        f.write(srt.compose(transcribtedText))
        f.close()

    def GenerateSubtitle(self):
        transcribtedText = self.Transcribe()
        self.CreateSubtitle(transcribtedText)
        print("Done")
        print(self.DirForSaving[0:-4] + "(" + self.uuid + ")" + ".srt")


@app.route('/mp3/<filename>/<model>')
def my_link(filename, model):
    print(filename)
    # get real file name
    newfilename = ""
    for i in filename:
        if i == "-":
            newfilename += "/"
        else :
            newfilename += i

    # copy file to new path for recognizing
    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path[:-25] + "\n")

    model_path = ""
    if model == "FA":
        model_path = full_path[:-25] + "model(FA)"
    elif model == "EN":
        model_path = full_path[:-25] + "model(EN)"
    else:
        new_model_path = ""
        for i in model:
            if i == "-":
                new_model_path += "/"
            else :
                new_model_path += i
        model_path = new_model_path

    print(full_path[:-25] + "model(FA)")

    try:
        new_path = shutil.copy2(newfilename, ( "/" + full_path[:-25] + "audio/mp3"))#25

        new_filename = new_path[1:len(new_path)]
        print(new_filename)
        rec = VoiceRecognizer(new_filename , 7,model_path, newfilename)
        rec.GenerateSubtitle()

        if os.path.exists(new_path):
            os.remove(new_path)

        return (newfilename[:-4] + "(" + rec.uuid + ").srt")
    except Exception as e:
        return ("Error:" + str(e))


from moviepy.video.io.VideoFileClip import VideoFileClip

@app.route('/mp4/<filename>/<model>')
def my_link2(filename, model):
    newfilename = ""
    for i in filename:
        if i == "-":
            newfilename += "/"
        else :
            newfilename += i

    try:
        full_path = os.path.realpath(__file__)

        model_path = ""
        if model == "FA":
            model_path = full_path[:-25] + "model(FA)"
        elif model == "EN":
            model_path = full_path[:-25] + "model(EN)"
        else:
            new_model_path = ""
            for i in model:
                if i == "-":
                    new_model_path += "/"
                else :
                    new_model_path += i
            model_path = new_model_path

        new_path = shutil.copy2(newfilename, ( "/" + full_path[:-25] + "audio/mp4"))

        new_filename = "." + new_path[1:len(new_path)]

        path_for_audio = (str(new_path)[0:-4]) + ".mp3"

        video = VideoFileClip(newfilename)
        video.audio.write_audiofile(path_for_audio)
        rec = VoiceRecognizer(path_for_audio , 7, model_path, newfilename)
        rec.GenerateSubtitle()
        if os.path.exists(new_path) and os.path.exists(path_for_audio):
            os.remove(new_path)
            os.remove(path_for_audio)

        return (newfilename[:-4] + "(" + rec.uuid + ").srt")
    except Exception as e:
        return ("Error:" + str(e))


@app.route('/convert/<filename>/<outputFormat>')
def convert(filename, outputFormat):
    newfilename = ""
    print("here")
    for i in filename:
        if i == "-":
            newfilename += "/"
        else :
            newfilename += i

    try:

        FileNameForConverting, FileExtension = os.path.splitext(newfilename)

        print(FileNameForConverting)
        print(FileExtension)
        print(newfilename)

        fileExe = str(FileExtension)[1:len(str(FileExtension))]

        print(fileExe)
        print(os.path.normpath(newfilename))
        print(outputFormat[1:len(outputFormat)])
        if fileExe == "wave" :
            song = AudioSegment.from_wav(newfilename)
            song.export(FileNameForConverting + outputFormat,format = outputFormat[1:len(outputFormat)])
            print("done")
            return (FileNameForConverting + FileExtension)

        elif fileExe == "mp3" :
            sound = AudioSegment.from_mp3(newfilename)
            sound.export(FileNameForConverting + outputFormat, format=outputFormat[1:len(outputFormat)])
            print("done")
            return (FileNameForConverting + outputFormat)

        else:
            audio = AudioSegment.from_file(newfilename, FileExtension[1:len(FileExtension)])
            audio.export(FileNameForConverting + outputFormat, format=outputFormat[1:len(outputFormat)])
            print("done")
            return (FileNameForConverting + outputFormat)

    except Exception as e:
        print(e,"eror")
        return "Error" + str(e)

@app.route('/translate/<filedir>/<lang>')
def translate(filedir, lang):
    simpleFileDir = ""
    for i in filedir:
        if i == "-":
            simpleFileDir += "/"
        else :
            simpleFileDir += i
    try:
        SavingFileDir, FileExtension = os.path.splitext(simpleFileDir)
        uuidForFile = str(uuid.uuid4())

        print(os.path.exists(simpleFileDir), (os.path.exists(SavingFileDir + "(" + uuidForFile + ")" + ".srt")))
        if (os.path.exists(simpleFileDir) and FileExtension == ".srt" and not(os.path.exists(SavingFileDir + "(" + uuidForFile + ")" + ".srt"))):
            with open(simpleFileDir) as file:
                subtitle = file.readlines()
                sub_list = [subtitle[i : i+4] for i in range(0, len(subtitle), 4)]
                subtitle_timeـdict = []
                word_for_translate = []
                subtitme_number_dict = []
                s = ""

                for item in sub_list:
                    subtitme_number_dict.append(item[0].strip("\n"))
                    subtitle_timeـdict.append(item[1].strip('\n'))
                    word_for_translate.append(item[2].strip('\n'))

                result = translator.translate(word_for_translate, src='en', dest='fa')

                i = 0
                for phrase in result:
                    s += (subtitme_number_dict[i] + "\n")
                    s += (subtitle_timeـdict[i] + "\n")
                    s += (phrase.text + "\n")
                    s += "\n"
                    i += 1

                f = open(SavingFileDir + "(" + uuidForFile + ")" + ".srt", "w")
                f.write(s)
                print("done")
                return (SavingFileDir + "(" + uuidForFile + ")" + ".srt")
        else:
            raise Exception("File dir error, Please choose another file format or change your subtitle file directory without spaces")

    except Exception as e:
        print("error", e)
        return "Error" + str(e)


@app.route('/')
def hello():
    return "Welcome to Voisy backend!"


if __name__ == '__main__':
  app.run(debug=True, port=5000)
