import speak as s
import takingcommand as t
import database as d



def registration():
    while True:
        try:
            s.speak("registration name please")
            regname=t.takeCommand()
            s.speak("registration password please")
            regpas=t.takeCommand()
            #print(regname,regpas)
            s.speak("Reconform your  details please")
            s.speak("your name is"+regname)
            s.speak("your password is"+regpas)
            s.speak("please tell yes to conform, no to retry,exit to terminate from here")
            conform=t.takeCommand()
            if(conform=='yes'):
                s.speak("inserting your details in database")
                d.mycur.execute(f"insert into xyz values('{regname}','{regpas}')")
                s.speak("you are successfully registered to use jarvis")
                break


            elif'no' in conform:
                s.speak("Okay.... retrying your registration process....... your")
                #print("no")
                registration()
                break

            elif 'exit' in conform:
                s.speak('okay, terminating registration process')
                break
            else:
                s.speak('looks like you spoke something else ')
                s.speak('i will terminate registration process from here ')
                break
        except:
            s.speak("speak louder Sir...")
            # registration()


