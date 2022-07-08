"""
iNeuron
"""

import threading
import time

start = time.perf_counter()

def Sleeping_Example(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return print(f'Done Sleeping...{seconds}')

## Setting up multiple threads
t1=threading.Thread(target=Sleeping_Example(1))
t2=threading.Thread(target=Sleeping_Example(1))
t3=threading.Thread(target=Sleeping_Example(1))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')