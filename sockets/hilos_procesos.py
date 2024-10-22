from time import sleep
from threading import Thread



def hello():
    while True:
        print('hola')
        sleep(1)

def world():
    while True:
        print('mundo')
        sleep(0.5)

t1 = Thread(target=hello)
t2 = Thread(target=world)

t1.start()
t2.start()