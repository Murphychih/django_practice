from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def user(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        print(request.POST)
        code = "0"
        msg = "用户添加成功"
        result = {"code": code, "msg": msg}
        return JsonResponse(result)
