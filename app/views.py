from django.shortcuts import render
import re



def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']


        context = {"answer": action}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": "answer"}
        return render(request, 'app/index.html', context=context)



