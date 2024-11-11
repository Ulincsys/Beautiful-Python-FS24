# https://docs.python.org/3/library/threading.html
from threading import Thread, Lock
import time

def run_forever(lock: Lock):
    while True:
        if not lock.locked():
            # Will try to acquire lock
            # will block if lock is already acquired
                # Will wait forever until lock is released
            lock.acquire()
        else:
            lock.release()
        time.sleep(5)

lock = Lock()
t = Thread(target=run_forever, args=[lock], daemon=True)
t.start()

print("Acquire lock in main thread")
lock.acquire()
print("Lock acquired")