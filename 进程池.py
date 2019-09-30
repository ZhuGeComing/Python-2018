from  multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print('进程：%d'%os.getpid())
    startTime = time.time()
    time.sleep(2)
    stopTime = time.time()
    print('子进程：%d,花费时间:%d'%(msg,stopTime-startTime))

#创建进程池

pool = Pool(3)

for x in range(10):
    pool.apply_async(worker,(x,))

#关闭进程池

pool.close()

#父进程等待进程结束

pool.join()

print('进程池已经结束')