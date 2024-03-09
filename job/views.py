from django.shortcuts import render

from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<center>Hello, world. You're at the jobs homepage.</center>")
