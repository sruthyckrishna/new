from ast import operator
from unittest import result
from django.shortcuts import render

# Create your views here.
def loadfirst(request):
    return render(request,'calculator.html')

def equal(request):
    n1=int(request.POST.get('num1'))
    n2=int(request.POST.get('num2'))
    operator=request.POST.get('oper')
    if operator=='+':
        out=n1+n2
    elif operator=='-':
        out=n1-n2
    elif operator=='*':
        out=n1*n2
    elif operator=='/':
        out=n1/n2
    return render(request,'calculator.html',{'result':out})
        
