import  re
import requests


def OneMusic (url):

    # url = 'http://ibaotu.com/sucai/584223.html'

    music_text = requests.get(url)

    music_div = re.findall(r'<div class="audio-box clearfix">(.*?)<div class="time-bar">', music_text.text, re.S)

    music_name = re.findall(r'8"><title>(.*?)_【包图网】</titl', music_text.text, re.S)

    music_url = re.findall(r'source src="(.*?)"></audio>', music_div[0], re.S)

    music = requests.get(music_url[0])

    with open(music_name[0] + '.mp3', 'wb') as  f:

        f.write(music.content)

url = 'http://ibaotu.com/yinxiao/10-91512-0-0-0-1.html'

url_text = requests.get(url)

url_list = re.findall(r'<ul class="clearfix sucai_list">(.*?)<div class="pagelist"> ',url_text.text,re.S)

url_all = re.findall(r'<div class="audio-info"><a href="(.*?\.html)" target="_blank" class="audio-name">.*?</a>',url_list[0],re.S)

for music_url in url_all:

    OneMusic(music_url)


