import threading
from time import sleep
import os

numPhilosophers = 5
porcie = 5
philosophers = []
forks = []
mutex = Semaphore()


class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        global porcie

    def run(self):
        leftForkIndex = self.index
        rightForkIndex = (self.index + 1) % numPhilosophers
        forkPair = ForkPair(leftForkIndex, rightForkIndex)

        # jedenie filozofa
        self.filozof_je(self.index, forkPair)

    def filozof_je(self, i, forkPair):
        # Jedenie
        while True:
            print("Thinking {} philosoph".format(i))
            sleep(0.5)
            forkPair.get_forks()
            print("Filozof papa  ", i)
            sleep(0.5)
            forkPair.put_forks()


class ForkPair:
    def __init__(self, leftFork, rightFork):
        # prevencia deadlocku
        if leftFork > rightFork:
            leftFork, rightFork = rightFork, leftFork
        self.firstFork = forks[leftFork]
        self.secondFork = forks[rightFork]

    def get_forks(self):
        self.firstFork.acquire()
        self.secondFork.acquire()

    def put_forks(self):
        self.firstFork.release()
        self.secondFork.release()


if __name__ == "__main__":

    # vytvorenie filozofov a vidliciek
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i))
        forks.append(threading.Lock())  # naplnenie semaformi

    for philosopher in philosophers:
        philosopher.start()

    # ukoncenie programu pomocou ctr+C
    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)

