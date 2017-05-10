from threading import Thread, Semaphore, Lock
from random import randint
from time import sleep

"""
majme vecerajucich filozofov spolu s manzelkami a detmi. 
o deti sa staraju sarmantne asistentky, 
vzdy musi byt k dispozicii 1 na 3 deti. 
manzelky rady chodia ku kadernikovi a filozofi pocas svojej rozpravy duchaju fajky 
(na tie potrebuju zapalovac, tabak a samozrejme fajku). nakolko filozofi jedia zo spolocneho hrnca, 
ten sa im obcas vyprazdni, a na jeho naplnenie maju kuchara - toho vzdy zobudia, 
ked je hrniec prazdny. v dome je vsak iba jedno spolocne wc, a tak treba zabezpecit,
 aby ho v jednom case nepouzivali osoby rozneho pohlavia.
  filozofi premyslaju nad otazkou zmyslu zivota, vesmiru a vobec, a na tuto temu pisu knihu. 
  ked niekto nieco napise, dalsi skontroluju. obcas sa vsak stane, ze k stolu pribehne dieta, 
  a vytrhne nejaku tu stranku z knihy.
"""

nFilozofov = 5
nZien = 5
nDeti = 3
nAsistentky = 1

filozofi = []
zeny = []
deti = []
asistentky = []
vidlicky = []


class Filozof(Thread):
    def __init__(self,index):
        Thread.__init__(self)
        self.index = index

    def run(self):
        leftForkIndex = self.index
        rightForkIndex = (self.index + 1) % nFilozofov
        forkpair = ForkPair(leftForkIndex,rightForkIndex)


        while True:
            self.jedenie(self.index,forkpair)

    def fajci(self):
        pass

    def jedenie(self, i, forkPair):
        print("Thinking {} philosoph".format(i))
        sleep(0.5)
        forkPair.get_forks()
        print("Filozof je ", i)
        sleep(0.5)
        forkPair.put_forks()



    def pisanie(self):
        pass

    def ide_na_wc(self):
        pass

class ForkPair:
    def __init__(self,lava, prava):
        if lava > prava:
            lava, prava = prava, lava
        self.prva = vidlicky[lava]
        self.druha = vidlicky[prava]

    def get_forks(self):
        self.prva.acquire()
        self.druha.acquire()

    def put_forks(self):
        self.prva.release()
        self.druha.release()


class Manzelka(Thread):
    def __init__(self,index):
        Thread.__init__(self)
        self.index = index


class Dieta(Thread):
    def __init__(self,index):
        Thread.__init__(self)
        self.index = index

class Asistentka(Thread):
    def __init__(self,index):
        Thread.__init__(self)
        self.index = index

class Kadernik(Thread):
    def __init__(self,index):
        Thread.__init__(self)
        self.index = index

class Kuchar(Thread):
    def __init__(self, index):
        Thread.__init__(self)
        self.index = index



if __name__=="__main__":


    for i in range(0,nFilozofov):
        filozofi.append(Filozof(i))

        vidlicky.append(Lock())


    print(filozofi)
    for filozof in filozofi:
        filozof.start()


