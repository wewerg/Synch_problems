"""
Problem SEARCH-INSERT-DELETE

"""
import os
import threading
import sys
from time import sleep
import lightswitch
from random import randint


def deleter():
    while True:
        noInsert.acquire()
        noSearch.acquire()

        #ko
        print("Mazem")
        sleep(2)


        noSearch.release()
        noInsert.release()


def inserter():
    while True:
        insertLS.lock(noInsert)
        insertMutex.acquire()
        #KO
        print("vkladam ")
        sleep(1)
        insertMutex.release()
        insertLS.unlock(noInsert)




def searcher():
    while True:
        searchLS.lock(noSearch)
        print("chcem hladat")
        sleep(3)
        searchLS.unlock(noSearch)
    pass


def workwithfile(subor, operacia):
    if operacia == "i":
        sleep(5)
        pass
    elif operacia == "s":
        sleep(5)
        pass
    elif operacia == "d":
        sleep(5)
        pass
    else:
        sys.stderr.write("neplatna volba")

    pass


if __name__ == "__main__":
    insertMutex = threading.Semaphore(1)

    noSearch = threading.Semaphore(1)
    noInsert = threading.Semaphore(1)
    searchLS = lightswitch.Lightswitch()
    insertLS = lightswitch.Lightswitch()


    for i in range(randint(1, 5)):
        threading.Thread(target=inserter).start()
    for i in range(randint(1, 5)):
        threading.Thread(target=deleter).start()
    for i in range(randint(1, 5)):
        threading.Thread(target=searcher).start()


    # pracuje s keyboard exception
    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
