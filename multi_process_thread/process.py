import os

print("Process {} start...".format(os.getppid()))
pid = os.fork()
if pid == 0:
    print("i am child process, my_pid:{}, my_parent_pid:{}".format(os.getpid(), os.getppid()))
else:
    print("i am parent process, my_pid:{}".format(os.getpid()))
