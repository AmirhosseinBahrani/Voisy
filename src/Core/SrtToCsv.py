import re

with open('audio/mp3/qe.srt', 'r') as h:
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

# Merge results
subs = {start_time:line for start_time,line in zip(start_times, lines)}
print(subs)