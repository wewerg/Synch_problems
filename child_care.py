from multiprocessing import Semaphore,Lock
import threading
from time import sleep
import logging
from random import randint
import os

"""jeden dospely musi mat max 3 deti"""

mutex = Lock()
multiplex = Semaphore(0)

logging.basicConfig(level=logging.WARNING,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def adult(i):
    while True:
        logging.debug('Starting')
        multiplex.release()
        multiplex.release()
        multiplex.release()

        print("Staram sa o deti")
        sleep(1)
        mutex.acquire()
        multiplex.acquire()
        multiplex.acquire()
        multiplex.acquire()
        mutex.release()
        logging.debug('Stopping')



def child(i):
    logging.debug('Starting')
    while True:
        multiplex.acquire()
        print("som dieta {} a hram sa".format(i))
        multiplex.release()
        sleep(randint(1, 3))
    logging.debug('Stopping')


if __name__ == "__main__":


    deticky =[]
    rodicia = []


    for i in range(10):
        deticky.append(threading.Thread(target=child, args=(i,)))

    for i in range(1):
        rodicia.append(threading.Thread(target=adult, args=(i,)))

    [rodic.start() for rodic in rodicia]
    [dieta.start() for dieta in deticky]



    #vlakno.join()
    #[dieta.join() for dieta in deticky]



"""
    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
"""