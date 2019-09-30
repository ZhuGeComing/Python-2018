import os
pid = os.fork()


if pid < 0:
    print('调用失败')
elif pid == 0:
    print('子进程：%d,父进程：%d'%(os.getpid(),os.getppid()))
else:
    print('父进程:%d,子进程:%d'%(os.getpid(),pid))