import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('Sekarang jam!')
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak('Sekarang Tahun, Bulan, Tanggal!')
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Halo Tuan Revian')
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour>=1 and hour<9:
        speak('Selamat Pagi Tuan Revian!')
    elif hour>=9 and hour<14:
        speak('Selamat Siang Tuan Revian!')
    elif hour>=14 and hour<19:
        speak('Selamat Sore Tuan Revian!')
    else:
        speak('Selamat Malam Tuan Revian!')

    speak('Revd007 adalah ciptaan Tuan Revian. Tolong katakan apa yang bisa saya bantu hari ini!')
    
def perintah():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Mendengarkan....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Memprosses....')
        query = r.recognize_google(audio,language='en-US')
        query = r.recognize_bing(audio, language='id-ID')
        print(query)

    except Exception as e:
        print(e)
        print('Tolong ulangi perintah anda....')
        return 'none'
    return query

wishme()
perintah()