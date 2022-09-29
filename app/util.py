from gtts import gTTS
from playsound import playsound



def count(text):
    try:
        if '/' in text:
            splt = text.split('/')
            result = int(splt[0]) / int(splt[1])
        elif '*' in text:
            splt = text.split('*')
            result = int(splt[0]) * int(splt[1])
        elif '+' in text:
            splt = text.split('+')
            result = int(splt[0]) + int(splt[1])
        elif '-' in text:
            splt = text.split('-')
            result = int(splt[0]) - int(splt[1])
        else:
            return 'Unsupported operation'
    except Exception:
        return 'Unsupported operation'
    else:
        return result

def say(text):
    language = 'en'
    text_val = text
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save("answer.mp3")
    playsound("answer.mp3")

