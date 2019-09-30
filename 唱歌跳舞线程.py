import  threading
from time import *
def sing():
    for i in range(3):
        print('正在唱歌%d'%i)
        sleep(1)

def dance():
    for i in range(3):
        print('我正在跳舞%d'%i)
        sleep(2)

st = threading.Thread(target=sing)

dt = threading.Thread(target=dance)

st.start()

dt.start()

while True:

    length = len(threading.enumerate())

    print('当前正在运行的有%d'%length)

    if length <= 1:
        break

    sleep(0.5)
