from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name="Utkarsh"
    return render(request,"home.html",{"name":name})

def add(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    res=num1+num2
    return render(request,"result.html",{'result':res})
