"""
iNeuron
"""

import multiprocessing
import time

start = time.perf_counter()

def Sleeping_Example(seconds):
    print(f'Sleeping {seconds} second(s).')
    time.sleep(1)
    print('Done Sleeping')

if __name__ == '__main__':
    multiprocessing_list = []## Creating a list of multiprocessing
    for _ in range(3): ## Function is called here 3 times
        p = multiprocessing.Process(target=Sleeping_Example ,args=[1]) ## args=1, passing 1 second
        p.start()
        multiprocessing_list.append(p) ## Adding each processing in the list

    ## Performing joining operation to insure it finishes all multiprocessing, 
    ## then it go below for further execution
    for process in multiprocessing_list:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')