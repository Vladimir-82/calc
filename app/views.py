from django.shortcuts import render
from .util import *


def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        result_num = count(action)
        say(str(result_num))

        context = {"answer": result_num}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "answer"}
        return render(request, 'app/index.html', context=context)


