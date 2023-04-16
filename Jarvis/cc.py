import clap as c
import threading
import  mains as ms








while True:
    if(c.t5.is_alive()==False):
        c.t5.start()
    if(ms.t9.is_alive()==False):
        ms.t9.start()
    if(c.t5.is_alive()==True):
        print('t5==', c.t5.is_alive())
        c.t5.join()
    if(ms.t9.is_alive()==True):
        print('t9==', ms.t9.is_alive())
        ms.t9.join()

