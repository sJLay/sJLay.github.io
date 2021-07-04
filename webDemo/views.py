from django.shortcuts import render
from dbDemo.models import DbDemo

def webdemo(request):
    # user = DbDemo.objects.all()
    result = {'statu': 'success'}
    if request.method == 'POST' and request.POST:
        name = request.POST.get('name')
        password = request.POST.get('password')
        nameIndb = DbDemo.objects.filter(name=name)
        passwordIndb = DbDemo.objects.filter(password=password).first()
        user = {'username':name,'userpassword':password}
        # user = {'username':name}
        if nameIndb and passwordIndb:
            # return render(request,'webDemo/success.html', {'name':name})
            return render(request,'webDemo/success.html',{'user':user})
        else:
            result['statu'] = 'error'
    return render(request,'webDemo/webDemo.html',{'result':result})

# Create your views here.
