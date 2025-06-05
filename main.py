import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[-1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=10,phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-In')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say again please...")
        print(e)
        return "none"
    return query


def main():
    speak("Hello Janil")
    query = takecommand().lower()

if __name__ == "__main__":
    main()
