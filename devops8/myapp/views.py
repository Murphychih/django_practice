from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from myapp.models import User, Project, Server, App
from django.core import serializers
import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def self_login_required(func):
    def inner(request):
        is_login = request.session.get('is_login', False)
        if not is_login:
            return redirect(login)
        else:
            return func(request)
    return inner



@self_login_required
def index(request):
    # res = User.objects.create(user='along', name='阿龙', sex='男', age=27, label='老司机')
    return render(request, 'index.html')





def user_add(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        print(request.POST)
        user = request.POST.get("user", None)
        name = request.POST.get("name", None)
        sex = request.POST.get("sex", None)
        age = request.POST.get("age", None)
        label = request.POST.get("label", None)

        User.objects.create(user=user, name=name, sex=sex, age=age, label=label)
        return HttpResponse("POST ")


def api(request):
    obj = User.objects.all()
    data = serializers.serialize('json', obj)
    # return HttpResponse(data)
    d = {}
    for i in obj:
        d['name'] = i.name
        d['user'] = i.user
        d['age'] = i.age
        d['sex'] = i.sex
    return JsonResponse(d)


def onetoone(request):
    user_obj = User.objects.get(user='along')

    return render(request, "onetoone.html", {'user': user_obj})


def app(request):
    app_list = App.objects.all()
    return render(request, 'app.html', {'app_list': app_list})


def project(request):
    project_list = Project.objects.all()
    return render(request, 'project.html', {'project_list': project_list})


def app_add(request):
    if request.method == "GET":
        project_list = Project.objects.all()
        server_list = Server.objects.all()
        return render(request, 'app_add.html', {'project_list': project_list, 'server_list': server_list})
    elif request.method == "POST":
        print(request.POST)
        server_list = request.POST.getlist("server_list", None)
        name = request.POST.get('app-name', None)
        describe = request.POST.get('app-describe', None)
        project = request.POST.get('project-name', None)
        project_obj = Project.objects.get(name=project)
        app = App.objects.create(name=name, describe=describe, project=project_obj)
        for server in server_list:
            server = Server.objects.get(hostname=server)
            server.app.add(app)
        return HttpResponse("Succeed")


def server(request):
    server_list = Server.objects.all()
    return render(request, 'server.html', {"server_list": server_list})


def project_app_server(request):
    app_list = App.objects.all()
    return render(request, 'project_app_server.html', {"app_list": app_list})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            auth.login(request, user)
            return redirect(index)
        else:
            msg = "用户密码错误"
        return render(request, "login.html", {"msg": msg})


def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect(login)
