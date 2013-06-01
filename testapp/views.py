from django.http import HttpResponse
from celery import Celery

def home(request):
    return HttpResponse('home')
