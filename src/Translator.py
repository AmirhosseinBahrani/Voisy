from translate import Translator
translator= Translator(from_lang="persian",to_lang="english")
translation = translator.translate("سلام")
print(translation)

with open('audio/mp3/qe.srt') as file:
    subtitle = file.readlines()
    sub_list = [subtitle[i : i+4] for i in range(0, len(subtitle), 4)]
    subtitle_dict = {}
    for item in sub_list:
        number = item[0].strip('\n')
        subtitle_dict[number] = item[2].strip('\n')
        subtitle_dict[f"{number}time"] = item[1].strip('\n')
        
    print(subtitle_dict)
