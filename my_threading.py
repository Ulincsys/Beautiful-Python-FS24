# https://docs.python.org/3/library/threading.html
from threading import Thread
import time

def threaded_hello(num = None):
    time.sleep(1)
    print(f"Hello from {num}")

print("Creating threads")

threads: list[Thread] = []
for i in range(3):
    # Create a thread which will run the provided target callable
    t = Thread(target=threaded_hello, args=[i])
    
    # Spin up the thread
    t.start()
    threads.append(t)
    # t.join()

print("Done creating threads")