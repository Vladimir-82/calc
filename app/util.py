import os

from gtts import gTTS
from playsound import playsound


def count(text):
    if '/' in text:
        splt = text.split('/')
        return int(splt[0]) / int(splt[1])
    elif '*' in text:
        splt = text.split('*')
        return int(splt[0]) * int(splt[1])
    elif '+' in text:
        splt = text.split('+')
        return int(splt[0]) + int(splt[1])
    elif '-' in text:
        splt = text.split('-')
        return int(splt[0]) - int(splt[1])
    else:
        return 'Unsupported operation!!'


def say(text):
    language = 'en'
    text_val = text
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save("answer.mp3")
    os.system("answer.mp3")