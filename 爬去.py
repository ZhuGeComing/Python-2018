import  requests
import re

url_text = requests.get('http://ibaotu.com/yinxiao/10-91512-0-0-0-1.html')



print(url_text.text)