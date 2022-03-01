
from googletrans import Translator
translator = Translator()

with open('/Users/amirhosseinsmacbookpro/Documents/Voisy/src/Core/audio/mp3/Q2(eb57762d-b0f4-441d-9c6e-25e2fde3acb2).srt') as file:
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

    f = open("/Users/amirhosseinsmacbookpro/Documents/Voisy/src/Core/audio/translated.srt", "w")
    f.write(s)
    print(s)
