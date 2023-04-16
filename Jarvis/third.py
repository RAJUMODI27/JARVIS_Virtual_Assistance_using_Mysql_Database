import playsound as p
from threading import *
from tkinter import *
from tkvideo import tkvideo
from time import *




def run():
    while True:

        p.playsound('jarvis_mu.mp3')

        global stop_threads

        if stop_threads:
            break

class jarvis_intro(Thread):
    def run(self):
        try:
            p.playsound(sound='jarvis.mp3')

        except:
            print("exception called at intro")





class jarvis_video(Thread):
    def run(self):
        try:
            global w
            w = Tk()
            w.title("JARVIS")
            lblVideo = Label(w)
            lblVideo.pack()
            player = tkvideo("Matrixs.mp4",
                             lblVideo,
                             loop=1,
                             size=(400, 300))
            player.play()

            w.mainloop()
            # sleep(2)
        except:
            print("excpetion called at jarv_vdo")







t2=jarvis_video()
t2.start()
sleep(1)





