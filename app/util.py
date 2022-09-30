import vlc
from time import sleep



def count(text):
    try:
        if '/' in text:
            splt = text.split('/')
            if len(splt) > 2:
                result = '-1'
            else:
                result = int(splt[0]) / int(splt[1])
        elif '*' in text:
            splt = text.split('*')
            if len(splt) > 2:
                result = '-1'
            else:
                result = int(splt[0]) * int(splt[1])
        elif '+' in text:
            splt = text.split('+')
            if len(splt) > 2:
                result = '-1'
            else:
                result = int(splt[0]) + int(splt[1])
        elif '-' in text:
            splt = text.split('-')
            if len(splt) > 2:
                result = '-1'
            else:
                result = int(splt[0]) - int(splt[1])
        else:
            result = '-1'
    except Exception:
        return '-1'
    else:
        return result



def say(text):
    for i in text:
        if i == '1':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "one.wav")))
        elif i == '2':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "two.wav")))
        elif i == '3':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "three.wav")))
        elif i == '4':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "four.wav")))
        elif i == '5':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "five.wav")))
        elif i == '6':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "six.wav")))
        elif i == '7':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "seven.wav")))
        elif i == '8':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "eight.wav")))
        elif i == '9':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "nine.wav")))
        elif i == '0':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "zero.wav")))
        elif i == '-':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "minus.wav")))
        elif i == '.':
            number = vlc.MediaPlayer(''.join(("app/", "media/", "dot.wav")))
        number.audio_set_volume(100)
        number.play()
        sleep(1)