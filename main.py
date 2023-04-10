import pyautogui as pg
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
while True:
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru").lower()
            if "youtube" in query:
                pg.hotkey("winleft")
                pg.typewrite("chrome\n", 0.2 )
                pg.hotkey("ctrl", "t")
                pg.typewrite("www.youtube.com\n", 0.2)
            elif "игра" in query:
                pg.hotkey("ctrl", "alt", "u")
            elif "telegram" in query:
                pg.hotkey("ctrl", "alt", "t")
            elif "google" in query:
                pg.hotkey("winleft", "3")
            elif "google" in query:
                pg.hotkey("winleft", "r")
                pg.typewrite("cmd\n", 0.2)
                pg.typewrite("color 2\n", 0.2)
                pg.typewrite("cls\n", 0.2)

    except:
        print()


