from django.shortcuts import render
from .util import *


def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer_num = count(action)
        context = {"answer": answer_num}
        say(str(answer_num))
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "answer"}
        return render(request, 'app/index.html', context=context)


