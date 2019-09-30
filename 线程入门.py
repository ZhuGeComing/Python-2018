import threading
import time

def fun(num):
    print('线程执行'+str(i))
    time.sleep(2)

for i in range(5):
    t = threading.Thread(target=fun(i),args=(i+1,))
    t.start()