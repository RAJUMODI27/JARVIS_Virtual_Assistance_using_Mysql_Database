import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source,timeout=10)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f"user spoke: {query}\n")
    except:
        query = ""
    return query


