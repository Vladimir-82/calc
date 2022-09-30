from django.shortcuts import render
from .util import *


def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer_num = count(action)
        if isinstance(answer_num, int):
            context = {"answer": str(answer_num)}
            say(str(answer_num))
            return render(request, 'app/index.html', context=context)
        else:
            context = {"answer": 'Аперацыя не падтрымліваецца'}
            return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "answer"}
        return render(request, 'app/index.html', context=context)