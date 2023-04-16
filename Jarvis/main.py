import datetime
import speak as s
import takingcommand as t
import wikipedia
import webbrowser
import pywhatkit
import os
import pyjokes

import third as ts
import threading
import clap as cl
import mains as ms









def main(master):
    ts.stop_threads = False

    t10 = threading.Thread(target=ts.run)
    t10.start()

    while (True):

        try:
            s.speak("  give me any command sir ")
            query = t.takeCommand()
            if ('wikipedia'in query  or "who" in query):
                s.speak('Okay ,  i found something , it says ')
                if 'wikipedia'in query:
                    query = query.replace('wikipedia', '')
                elif 'something' in query:
                    query = query.replace('something','')
                elif 'who' in query:
                    query = query.replace('who','')

                results = wikipedia.summary(query, sentences=2)

                s.speak(results)
                print("query="+query)


            elif 'open youtube' in query.lower():
                s.speak('working on it , opening youtube ')
                webbrowser.open('youtube.com')
            elif 'open google' in query.lower():
                webbrowser.open('google.com')

            elif 'open fitgirl repack' in query.lower():
                webbrowser.open('fitgirl-repacks.site')
            elif 'open gmail' in query.lower():
                webbrowser.open('gmail.com')
            elif 'play song' in query.lower():
                song = query.replace('play song', '')
                pywhatkit.playonyt(song)
            elif "time" in query.lower():
                strtimes = datetime.datetime.now().strftime("%H:%M:%S")
                s.speak(f"{master} the time is {strtimes}")
            elif 'open spotify' in query.lower():
                os.startfile('C:\\Users\\rnmod\\AppData\\Roaming\\Spotify\\Spotify.exe')
            elif 'joke' in query.lower():
                my_joke=pyjokes.get_joke('en',category='neutral')
                s.speak(my_joke)
            elif 'create ' in query.lower():
                s.speak('Okay working on it')
                s.speak('Tell me the appropriate file name which you want me to create')
                fname = t.takeCommand()

                s.speak('Okay. what you want me to write inside it')
                data = t.takeCommand()
                f = open(fname, 'wt')
                f.write(data)
                s.speak("file successfully created")
                os.startfile(fname)
            elif 'read ' in query.lower():
                while True:
                    try:
                        s.speak('can u tell me the name of the file, which you want me to read it for you ')
                        fname = t.takeCommand()
                        f = open(fname, 'rt')
                        s.speak(f.readlines())
                        break
                    except:
                        s.speak(f"{master} im sorry to say, file with that name, does not exist ")
                        # s.speak("file does not exist")
                        s.speak("you want to create the file with that name  or you want to exit")
                        fi=t.takeCommand()
                        if "create" in fi:
                            # s.speak('Tell me the appropriate file name which you want me to create')
                            # fname = t.takeCommand()

                            s.speak('Okay. what you want me to write inside it')
                            data = t.takeCommand()
                            f = open(fname, 'wt')
                            f.write(data)
                            s.speak("file successfully created")
                            break

                        else:
                            break

            elif 'rest' in query.lower() or 'exit' in query.lower():

                s.speak("it was pleasure,   talking to you...  Sir ")
                ts.w.state(newstate='iconic')
                ts.stop_threads = True
                ms.stop_mains = False
                cl.stop_clap = False

                t10.join()



                print('going to brak')

                break

            elif 'screenshot' in query.lower():
                s.speak('by what name you want to save that screenshot')
                sc_name = t.takeCommand()
                s.speak('taking Screen shot')
                pywhatkit.take_screenshot(sc_name, 2, True)

            elif 'email' in query.lower():
                while True:
                    try:
                        s.speak('can you tell me his email address')
                        receiver_email=t.takeCommand()
                        receiver_email=receiver_email.replace('at the rate','@')
                        receiver_email=receiver_email.replace(" ","")
                        print(receiver_email)
                        s.speak('check you email address on console')
                        s.speak('tell me to yes to continue, or no to repeat you email address')
                        c=t.takeCommand()
                        if 'yes' in c:
                            s.speak('what you want to write inside subject')
                            receiver_subject=t.takeCommand()
                            s.speak('what message you  want me to send him')
                            receiver_message=t.takeCommand()
                            # pywhatkit.send_mail('rnmodi27x@gmail.com', 'zrnhmiowbhjjbryp', receiver_subject, receiver_message, receiver_email)
                            s.speak('email sended successfully')
                            s.speak('waiting for new command ')
                            break
                        elif 'no' in c:
                            s.speak('okay,repeating entire process')
                            pass
                        else:
                            s.speak('well it seems like you spoke something else, .. i will take new command ')
                            break

                    except:
                        pass
            elif 'search' in query.lower():
                s.speak("Sir, what you want me to search")

                x = t.takeCommand()
                pywhatkit.search(x)
                # webbrowser.open(x)
            else:
                s.speak(" Well, Sir, It seems like you  had not programed me to do that ")



        except:
            s.speak(" ")

