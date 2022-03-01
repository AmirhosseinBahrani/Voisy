from pydub import AudioSegment
import os
from pathlib import Path

#"/Users/amirhosseinsmacbookpro/Music/iTunes/iTunes Media/Music/Billie Eilish & Khalid/Lovely Single/Lovely.mp3"
#"/Users/amirhosseinsmacbookpro/Downloads/Ofi_La_Melodia_Boom_320.mp3"

corrected_filename = ""
for i in "/Users/amirhosseinsmacbookpro/Music/iTunes/iTunes Media/Music/Billie Eilish & Khalid/Lovely Single/Lovely.mp3":
    if i == " ":
        corrected_filename += "\ "
    else:
        corrected_filename += i

print(corrected_filename)
FileNameForConverting, FileExtension = os.path.splitext(corrected_filename)
sound = AudioSegment.from_mp3(corrected_filename)
sound.export(FileNameForConverting + ".wav", format="wav")
