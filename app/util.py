import vlc
from time import sleep



def count(text: str):
    try:
        if '/' in text:
            splt = text.split('/')
            result = float(splt[0]) / float(splt[1])
        elif '*' in text:
            splt = text.split('*')
            result = float(splt[0]) * float(splt[1])
        elif '+' in text:
            splt = text.split('+')
            result = float(splt[0]) + float(splt[1])
        elif '-' in text:
            splt = text.split('-')
            result = float(splt[0]) - float(splt[1])
        else:
            result = '-1'
    except Exception:
        return '-1'
    if len(splt) > 2:
        return '-1'
    else:
        return result



def say(text: str) -> None:
    meaning = {'1': 'one', '2': 'two','3': 'three','4': 'four','5': 'five',
               '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
               '0': 'zero', '.': 'dot', '-': 'minus',
              }
    for i in text:
        treck = meaning.get(i)
        path = ''.join(('https://github.com/Vladimir-82/speach/blob/master/'
                        'sounds_blr/', treck, '.wav?raw=true')
                       )
        number = vlc.MediaPlayer(path)
        number.audio_set_volume(100)
        number.play()
        sleep(1)