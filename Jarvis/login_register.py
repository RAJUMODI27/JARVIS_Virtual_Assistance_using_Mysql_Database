import speak as s
import takingcommand as t
import registration as r
import login as l



def login_reg():
    while True:
        try:
            command=t.takeCommand()
            if 'register' in command:
                s.speak("registration process initiated")
                r.registration()
                s.speak("now u can easily login")
                s.speak("do u want to login or exit")
                while True:
                    y=t.takeCommand()
                    if 'login' in y:
                        i=l.login()
                       # master=i
                        # wishMe()
                       # return i
                        break
                    elif 'exit' in y:
                        s.speak("have a nice day.. sir")
                        break
                    else:
                        s.speak("is it login or exit sir can you please repeat")
                return i
            elif 'login' in command:
                s.speak("initiating login process")
                i=l.login()
                # master=i
                # wishMe()
                # return i
                break
            else:
                s.speak("can you please repeat sir")
                # l.login_reg()
                # break
        except:
            s.speak("Are you there sir...  Can you please tell me to register or login ")
    return i
