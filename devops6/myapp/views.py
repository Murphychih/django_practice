from django.shortcuts import render, HttpResponse, redirect
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
# Create your views here.

def index(request):
    # print(request.scheme)
    # print(request.body)
    # print(request.path)
    # print(request.method)
    # print(request.GET)
    # print(request.POST)
    # print(request.COOKIES)
    # print(request.session)
    # print(request.META)
    # print(request.META["HTTP_USER_AGENT"])
    # print(request.get_host())
    # print(request.get_port())
    # print(request.get_full_path())
    # print(request.get_raw_uri())
    # 获取URL参数
    # print(request.GET['id'])
    # print(request.GET['value'])
    # value = request.GET.get('value', None)
    # print(value)
    # req = request.GET
    # for i in req.items():
    #     print(i)

    res = HttpResponse("<h1>首页</h1>")
    res['name'] = 'aliang'
    res.status_code = 302
    return res

def hello(request):
    return HttpResponse("<h1>Hello Django</h1>")

def hello2(request):
    return HttpResponse("<h1>Hello MyAPP</h1>")

def logs(request):
    import os
    print(os.getcwd())
    project_dir = os.getcwd()
    #current_dir = os.path.join(project_dir, 'myapp')
    current_dir = os.path.dirname(os.path.abspath(__file__))  #  获取绝对路径
    with open(current_dir + '\\access.log',encoding='utf8') as f:
        result = f.read()
    return render(request, 'logs.html', {'result': result})

def test(request):
    return HttpResponse("Test!")

def year_archive(request, year):
    # 根据年份去数据库查询文章列表
    return HttpResponse("返回%s年文章列表" %year)

def month_archive(request, m,y):
    # 根据年份和月去数据库查询文章列表
    return HttpResponse("返回%s年%s月份文章列表" %(y,m))

def article_detail(request, year, month, id):
    return HttpResponse("查看ID为%s的文章" %(id))

def search(request):
    key = request.GET.get('key')
    result = "<h1>这是你查询的关键字%s的搜索结果...</h1>" %key
    return HttpResponse(result)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 获取用户通过POST提交的用户名和密码
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username)
        print(password)
        if username == "aliang" and password == "123456":
            # 登录成功
            # return redirect("/")
            return redirect(index)
        else:
            # 登录失败
            msg = "用户名或密码输入错误！"
            return render(request, 'login.html', {'msg': msg})

def user(request):
    if request.method == "GET":
        return render(request, 'user.html')
    elif request.method == "POST":
        print(request.FILES)
        obj = request.FILES.get('touxiang')
        file_name = obj.name
        import os
        file_path = os.path.join('upload', obj.name)
        with open(file_path, mode="wb") as f:
            for i in obj.chunks():
                f.write(i)
        msg = "上传文件成功"
        return  render(request, 'user.html', {"msg": msg})

def dt(request):
    from datetime import datetime
    dt = datetime.now()
    # return  render(request, 'dt.html', {'dt': dt})
    #return redirect("www.baidu.com")
    return redirect("/hello")

def upload_list(request):
    import os
    file_list = os.listdir('upload')
    return render(request, "upload_list.html", {'file_list': file_list})

def download(request, filename):
    import os
    file_path = os.path.join("upload", filename)
    #res = StreamingHttpResponse(open(file_path, 'rb'))
    res = FileResponse(open(file_path, 'rb'))
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment; filename=%s' %(os.path.basename(file_path))
    return res

def api(request):
    d = {'name': 'aliang','age':'30'}
    print(type(d))
    return JsonResponse(d)

def template(request):
    user = {'aliang': {'name': '阿良', 'sex': '男', 'age':30},
            'along': {'name': '阿龙', 'sex': '男', 'age': 28},
            'amei': {'name': '阿妹', 'sex': '女', 'age': 18},
            }
    return render(request, 'template.html', {'users': user} )


def about(request):
    return render(request, 'about.html')

def news(request):
    return  render(request, 'news.html')