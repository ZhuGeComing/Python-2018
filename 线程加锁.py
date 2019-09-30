import  threading
import time
g_num = 0
mutex = threading.Lock()
def worker():
    global  g_num
    for i in range(2000000):
        flag = mutex.acquire(False)
        if flag:
            g_num +=1
            mutex.release()

for i in range(2):
    t = threading.Thread(target=worker)
    t.start()

print(g_num)
