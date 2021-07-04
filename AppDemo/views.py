from django.shortcuts import render



def appTest(request):
    return render(request,'appDemo/index.html',locals())
# Create your views here.
