from django.shortcuts import render
from .util import *



def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer_num = count(action)
        if str(answer_num).endswith('.0'):
            answer_num = int(answer_num)
        context = {"answer": str(answer_num)}
        say(str(answer_num))
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "answer"}
        return render(request, 'app/index.html', context=context)