from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
import os
from django.db import connection

def home(request):
      return render(request, 'home.html')
