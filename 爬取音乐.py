
import requests

import re

url = 'http://ibaotu.com/sucai/584223.html'

music_text = requests.get(url)

music_div = re.findall(r'<div class="audio-box clearfix">(.*?)<div class="time-bar">',music_text.text,re.S)

music_name = re.findall(r'8"><title>(.*?)_【包图网】</titl',music_text.text,re.S)

music_url = re.findall(r'source src="(.*?)"></audio>',music_div[0],re.S)

music = requests.get(music_url[0])

with open (music_name[0] + '.mp3','wb') as  f:

    f.write(music.content)


