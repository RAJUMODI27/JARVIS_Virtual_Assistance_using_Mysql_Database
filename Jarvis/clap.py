import speak as s
import login_register as lr
import sounddevice as sd
import numpy as np
import  threading
import pyttsx3
import mains as ms
import main as m
import wishme as w
import third as ts
global stop_clap



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()




def detect_clap():
    while True:
        try:
            duration = 1.5  # seconds
            fs = 44100
            myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
            # print("Recording Audio...")
            sd.wait()
            # print("Audio recording complete , Play Audio")
            # sd.play(myrecording, fs)
            # sd.wait()
            # print("Play Audio Finished")
            audio = myrecording[:,0]
            clap_count = 0
            for i in range(len(audio)):
                if audio[i] > 0.5:
                    clap_count += 1
            if clap_count > 5:
                ms.stop_main = True

                ts.w.state(newstate='normal')
                print("Clap Detected")
                speak('Welcome BAck Sir ')
                s.speak("initiating Authenticating Phase....")
                s.speak(" do you would like to, login... or register")
                master = lr.login_reg()
                print("master=" + master)
                w.wishMe(master)
                s.speak("....sir .... is there anything i can do for you")
                m.main(master)


                t12=threading.Thread(target=ms.body)
                if t12.is_alive()==False:

                    t12.start()




            else:
                print("Clap Not Detected")




            if stop_clap:
                break



        except:
            pass
t5=threading.Thread(target=detect_clap)








