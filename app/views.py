from django.shortcuts import render
from .util import *



def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer_num = count(action)
        context = {"answer": str(answer_num)}
        say(str(round(answer_num, 8)))
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "answer"}
        return render(request, 'app/index.html', context=context)