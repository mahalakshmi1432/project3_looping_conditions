from django.shortcuts import render

# Create your views here.
def  conditions(request):
    d={'a':100,'b':300,'c':200}
    return render(request,'conditions.html',context=d)

def  nested(request):
    d={'a':50,'b':40,'c':30}
    return render(request,'nested.html',context=d)

def loops(request):
    d={'s':'mahalakshmi'}
    return render(request,'loops.html',context=d)