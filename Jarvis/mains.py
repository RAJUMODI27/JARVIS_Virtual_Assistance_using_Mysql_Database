
import speak as s
import takingcommand as t
import wishme as w
import login_register as lr
import threading

import main as m
import third as ts
import clap as c



global stop_main


def body():



    while True:




        try:


            wak=t.takeCommand()


            if "wake" in wak or 'uthe' in wak :
                c.stop_clap = True
                ts.w.state(newstate='normal')
                # t3 = ts.jarvis_intro()
                # t3.start()
                # t3.join()
                master="sir"
                #
                # s.speak("initiating Authenticating Phase....")
                s.speak(" do you would like to, login... or register")
                master = lr.login_reg()
                print("master="+master )
                w.wishMe(master)
                s.speak("....sir .... is there anything i can do for you")
                m.main(master)
                # c.stop_clap = False

                t15 = threading.Thread(target=c.detect_clap)
                t15.start()
                stop_main=False



            # elif "are you there" in wak:
            #
            #     ts.w.state(newstate='normal')
            #     s.speak("Yes Sir.. i am always here.. to serve you.. ")
            #     s.speak("initiating.. authorization phaze..")
            #     s.speak("Sir.., do you want to go for the  login or... registration process")
            #     master = lr.login_reg()
            #     w.wishMe(master)
            #     s.speak("hello sir .... is there anything i can do for you")
            #     m.main(master)




            # else:
            #     print("jarvis is still sleeping just you can call him by his command")

            if stop_main:
                break


        except:

            print('Jarvis is sleeping........')



t9 = threading.Thread(target=body)
