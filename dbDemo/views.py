from django.shortcuts import render
from dbDemo.models import DbDemo

def dbtest(request):
    # data = {'name': name, 'password': password}
    # list.append(data)
    result = ''#用于返回是否成功
    if request.method == 'POST' and request.POST:
        #判断提交方式是否为POST及POST是否有值
        name = request.POST.get('name')
        password = request.POST.get('password')
        db = DbDemo()
        db.name = name
        db.password = password
        db.save()
        result = 'success'
    return  render(request,'dbDemo/dbDemo.html',{'result':result})

def deleteUpdata(request):
    #删除模块
    result = {}
    if request.method == 'POST' and request.POST:
        name = request.POST.get('name')
        nameIndb = DbDemo.objects.filter(name=name).first()
        if nameIndb:
            nameIndb.delete()
            result['statu'] = 'success'
        else:
            result['statu'] = 'error'
    return render(request,'dbDemo/dbDemo1.html',{'result':result})

def changeData(request):
    #改变模块
    result = {}
    dbData = DbDemo.objects.all()
    result['data'] = dbData
    if request.method == 'POST' and request.POST:
        name = request.POST.get('name')
        nameIndb = DbDemo.objects.filter(name=name).first()
        if nameIndb:
            nameIndb.name = request.POST.get('name')
            nameIndb.password = request.POST.get('password')
            nameIndb.save()
            result['statu'] = 'success'
        else:
            result['statu'] = 'error'
    return render(request,'dbDemo/dbDemo2.html',{'result':result})

# def find(request):
#     result = {}
#     dbData = DbDemo.objects.all()
#     result['data'] = dbData
#     if request.method == 'POST' and request.POST:
#         name = DbDemo.objects.get('name')
#         password = DbDemo.objects.get('password')
#         result['statu'] = 'success'
#     return render(request, 'dbDemo/dbDemo3.html', {'result': result})

def find(request):
    people_list = DbDemo.objects.all()
    return render(request, 'dbDemo/dbDemo3.html',{'people_list':people_list})

    #查询模块
    # result = {'statu':'success'}
    # if request.method == 'POST' and request.POST:
    #     name = request.POST.get('name')
    #     nameIndb = DbDemo.objects.filter(name=name).first()
    #     if nameIndb:
    #         result['name'] = name
    #         result['password'] = nameIndb.password
    #         result['statu'] = 'success'
    #     else:
    #         result['statu'] = 'error'
    # return render(request, 'dbDemo/dbDemo3.html', {'result':result})




# Create your views here.
