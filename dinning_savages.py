from threading import Thread, Semaphore
from time import sleep
from random import randint

mutex = Semaphore()
prazdnyKS = Semaphore()
plnyKS = Semaphore(1)
porcie = 10


def divoch(id):
    global porcie
    while True:
        mutex.acquire()
        if porcie == 0:
            prazdnyKS.release()
            plnyKS.acquire()
        porcie -=1
        mutex.release()
        print("divoch {} papam".format(id))
        sleep(3)

def kuchar():
    global porcie
    while True:
        prazdnyKS.acquire()
        #varenie
        print("cakaj, vari sa")
        sleep(5)
        porcie = 10

        plnyKS.release()

if __name__=="__main__":




    kucharC = Thread(target=kuchar)
    kucharC.start()
    divosi = []
    for i in range(randint(10,20)):
        divochC = Thread(target=divoch,args=(i,))
        divosi.append(divochC)

    [div.start() for div in divosi]





    pass