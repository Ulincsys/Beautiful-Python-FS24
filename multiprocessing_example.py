from multiprocessing import Process, Queue
from os import getpid
from time import sleep
from random import random

def super_function(q, local_ID):
    print(f"Hello from: {getpid()} with local ID: {local_ID}")
    sleep(random())
    q.put((getpid(), local_ID))

if __name__ == '__main__':
    q = Queue()
    plist: list[Process] = []
    
    for i in range(8):
        p = Process(target=super_function, args=(q, i))
        p.start()
        plist.append(p)
        
    for i in range(8):
        pid, lpid = q.get()
        print(f"Process {pid} with local ID {lpid} exited")
        
    for p in plist:
        p.join()
