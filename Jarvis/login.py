import speak as s
import takingcommand as t
import database as d


def login():
    x1 = 3
    while (x1 > 0):
        try:
            s.speak("whats the user id")
            luser = t.takeCommand()
            s.speak("whats the password")
            lpassword = t.takeCommand()

            d.mycur.execute(f"select * from xyz where user like '{luser}'&& password like'{lpassword}'")
            #print(luser, lpassword)
            d.myresult = d.mycur.fetchall()
            #print(d.myresult)
            if (d.myresult != []):
                s.speak("authorization successsfull")

                # wishMe()
                return luser
                break
            if(d.myresult == []):
                # print("empty")
                x1 = x1 - 1
                s.speak(f"Login details Incorrect you got {x1} tries")

            for i in d.myresult:
                i
                break
            if (x1 == 0):
                s.speak("you are unauthorized ")
                break
        except:
            s.speak("speak louder... Sir")
