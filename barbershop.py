from threading import Semaphore,Thread
from random import randint
from time import sleep

customers = 0

def barber():
    while True:
        customerS.acquire()
        barberS.release()
        print("Ja si tu tak striham")
        sleep(2)
        cDone.acquire()
        bDone.release()

def customer():
    global  customers
    while True:
        mutex.acquire()
        if customers == pocet:
            mutex.release()
            pass
        customers +=1

        customerS.release()
        barberS.acquire()
        print("Som strihany")
        cDone.release()
        bDone.acquire()
        mutex.acquire()
        customers -= 1
        mutex.release()




        mutex.release()

if __name__ == "__main__":
    customerS = Semaphore(0)
    barberS = Semaphore(0)
    cDone = Semaphore()
    bDone = Semaphore()


    mutex = Semaphore(1)

    holic = Thread(target=barber)
    holic.start()

    pocet = randint(1,10)
    zakaznici = []
    print(pocet)
    for i in range(pocet):
        zakaznici.append(Thread(target=customer))


    for i in zakaznici:
        i.start()










    pass