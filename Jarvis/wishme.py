import datetime
import speak as s




def wishMe(master):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        s.speak("good Morning" +master)
    elif hour >= 12 and hour < 18:
        s.speak("Good Afternoon " +master)
    else:
        s.speak("good evening " + master)

