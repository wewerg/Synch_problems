from threading import Semaphore,Thread
from lightswitch import Lightswitch
from time import sleep
from random import randint

"""
Turniket:
s.acquire()
s.release()
"""


maleLs = Lightswitch()
femaleLs = Lightswitch()
maleS = Semaphore(3)
femaleS =Semaphore(3)
turniket = Semaphore(1)

def female(id):
    print("slecna {} pride do fronty".format(id))
    turniket.acquire()
    femaleLs.lock(empty)
    turniket.release()
    femaleS.acquire()
    #do bath
    sleep(randint(1,2))
    print("panicka {} pudruje nostek".format(id))
    femaleS.release()
    femaleLs.unlock(empty)
    print("panicka {} ide prec".format(id))


def male(id):
    print("chlapec {} pride do fronty".format(id))
    turniket.acquire()
    maleLs.lock(empty)
    turniket.release()
    maleS.acquire()
    # do bath
    sleep(randint(1, 2))
    print("chlapec {} cika".format(id))
    femaleS.release()
    femaleLs.unlock(empty)
    print("chlapec {} ide prec".format(id))


if __name__=="__main__":

    zenusky = []
    chlapi = []

    while True:
        pz = randint(4,10)
        print("zien mame {}".format(pz))
        pc = randint(4, 10)
        print("chlapcov mame {}".format(pc))

        for i in range(pz):
            zenuska = Thread(target=female, args=(i,))
            zenusky.append(zenuska)
            zenuska.start()


        for i in range(pc):
            chlap = Thread(target=male, args=(i,))
            chlapi.append(chlap)
            chlap.start()

        [zenuska.join() for zenuska in zenusky]
        [chlap.join() for chlap in chlapi]
