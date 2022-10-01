from django.shortcuts import render
from .util import *


def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer_num = count(action)
        if isinstance(answer_num, float):
            if str(answer_num).endswith('.0'):
                answer_num = str(answer_num)[:-2]
            context = {"answer": answer_num}
            say(str(answer_num))
            return render(request, 'app/index.html', context=context)
        else:
            context = {"answer": 'Аперацыя не падтрымліваецца'}
            return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "адказ"}
        return render(request, 'app/index.html', context=context)