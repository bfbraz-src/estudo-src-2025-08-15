from django.shortcuts import render
from django.http import HttpResponse

def tasks(request):
    return HttpResponse('Olá ao Tasks')

def taskslist(request):
    return render(request, 'list.html')

def yourName(request, name):
    return render(request, 'yourname.html', {'name':name}) 