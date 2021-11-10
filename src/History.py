import os
import time

class History :
    def __init__(self):
        self.src = ".\\audio\\mp3\\"
        self.recordedFilesSrc = ".\\audio\\records\\"
        self.otherFilesSrc = ".\\audio\\others\\"
    def getMp3Files(self):
        files = []
        for filename in os.listdir(self.src):
            if filename.endswith(".mp3"): 
                properties = [filename]
                path = ".\\audio\\mp3\\" + filename
                date = time.ctime(os.path.getmtime(path))
                properties.append(date)
                files.append(properties)
            else:
                continue

        return files
    def getRecordedFiles(self):
        files = []
        for filename in os.listdir(self.recordedFilesSrc):
            if filename.endswith(".mp3"): 
                properties = [filename]
                path = ".\\audio\\records\\" + filename
                date = time.ctime(os.path.getmtime(path))
                properties.append(date)
                files.append(properties)
            else:
                continue

        return files
    def getOtherFiles(self):
        files = []
        for filename in os.listdir(self.otherFilesSrc):
            
            properties = [filename]
            path = ".\\audio\\others\\" + filename
            date = time.ctime(os.path.getmtime(path))
            properties.append(date)
            files.append(properties)


        return files

