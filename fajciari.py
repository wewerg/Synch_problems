from threading import Semaphore,Thread
import os
from time import sleep


AgentS = Semaphore(1)

semZ = Semaphore()
semP = Semaphore()
semT = Semaphore()
semFZ = Semaphore()
semFP = Semaphore()
semFT = Semaphore()
muztex = Semaphore()
isPapier = False
isZapalky = False
isTabak = False



def Agent1():
    while True:
        AgentS.acquire()
        semT.release()
        semP.release()
        AgentS.release()

def Agent2():
    while True:
        AgentS.acquire()
        semZ.release()
        semP.release()
        AgentS.release()

def Agent3():
    while True:
        AgentS.acquire()
        semT.release()
        semZ.release()
        AgentS.release()

def fajciarT():
    while True:
        semZ.acquire()
        semP.acquire()
        #make cigarett
        print("fajciar T")
        AgentS.release()
        #mozem fajcit

        sleep(2)

def fajciarP():
    while True:
        semT.acquire()
        semZ.acquire()
        #make cigarett
        print("fajciar P")
        AgentS.release()
        #mozem fajcit
        sleep(2)


def fajciarZ():
    while True:
        semT.acquire()
        semP.acquire()
        # make cigarett
        print("fajciar Z")
        AgentS.release()
        # mozem fajcit
        sleep(4)

def pusherT():
    global isZapalky
    global isPapier
    global isTabak
    while True:
        semT.acquire()
        AgentS.acquire()
        if isZapalky:
            isZapalky = False
            semP.release()
        elif isPapier:
            isPapier = False
            semZ.release()
        else:
            isTabak = True
        AgentS.release()

def pusherP():
    global isZapalky
    global isPapier
    global isTabak
    while True:
        semP.acquire()
        AgentS.acquire()
        if isZapalky:
            isZapalky = False
            semT.release()
        elif isTabak:
            isTabak = False
            semZ.release()
        else:
            isPapier = True
        AgentS.release()

def pusherZ():
    global isZapalky
    global isPapier
    global isTabak
    while True:
        semZ.acquire()
        AgentS.acquire()
        if isTabak:
            isTabak = False
            semP.release()
        elif isPapier:
            isPapier = False
            semT.release()
        else:
            isZapalky = True
        AgentS.release()

if __name__=="__main__":

    Thread(target=Agent1).start()
    Thread(target=Agent2).start()
    Thread(target=Agent3).start()
    Thread(target=fajciarT).start()
    Thread(target=fajciarP).start()
    Thread(target=fajciarZ).start()
    Thread(target=pusherP).start()
    Thread(target=pusherT).start()
    Thread(target=pusherZ).start()



    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt,SystemExit):
        os._exit(0)




