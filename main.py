import pyautogui as pg
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
while True:
    tm = 0.1 #время, за которое должна ввестись команда
    alp = "йцукенгшщзхъфывапролджэячсмитьбю" #алфавит, для далнеешей проверки, сказанна команда или случайное слово
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru").lower() #устанавливаем язык для распозования и переводим в нижней регистр

            #есть слова, которые прога распознает на русском, меняйте под себя
            if "блендер" in query: query = "blender"
            if "питон" in query: query = "pycharm"
            if "цмд" in query: query = "cmd"
            if "java" in query: query = "IntelliJ IDEA"

            if query[0] not in alp:
                pg.hotkey("winleft")
                #win
                if "youtube" in query: pg.typewrite("chrome\n"+query+"\n", tm)#тут добовляете свои саейты
                else: pg.typewrite(query+"\n", tm)

                if "cmd" in query: pg.typewrite("\n\n\n\ncolor 2\ncls\n", tm)
            if "выключи комп" in query: pg.typewrite("cmd\n\n\n\n\n\nshutdown /s\n", tm)

            if "окна" in query:
                #pg.hotkey("winleft")
                pg.hotkey("winleft", "d")


    except:
        print('')





