from django.shortcuts import render
import requests


def req(request):
    if request.method == 'GET':
        return render(request, 'score.html')
