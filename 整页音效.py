import  re
import  requests


url = 'http://ibaotu.com/yinxiao/10-91512-0-0-0-1.html'

url_text = requests.get(url)

url_list = re.findall(r'<ul class="clearfix sucai_list">(.*?)<div class="pagelist"> ',url_text.text,re.S)

url_all = re.findall(r'<div class="audio-info"><a href="(.*?\.html)" target="_blank" class="audio-name">.*?</a>',url_list[0],re.S)

for music_url in url_all:




print(url_all)