"""devops6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path('^$', views.index),  # /index 访问
    path('hello', views.hello, name='hello'),  # /hello 访问
    path('logs', views.logs),    # /logs 访问
    path('test', views.test, name="test"),
    path('myapp/', include('myapp.urls')),
    re_path('articles/([0-9]{4})/$', views.year_archive),
    #re_path('articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    re_path('articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive),
    re_path('articles/([0-9]{4})/([0-9]{2})/([0-9]+)$', views.article_detail),
    re_path('search/$', views.search),
    re_path('login/$', views.login, name="login"),
    re_path('user/$', views.user, name="user"),
    re_path('dt/$', views.dt),
    re_path('upload_list/$', views.upload_list),
    re_path('download/(?P<filename>.*)/$', views.download, name='download'),
    re_path('api/$', views.api),
    re_path('template/$', views.template),
    re_path('about/$',views.about),
    re_path('news/$',views.news)
]

"""
文章归档案例：
http://ip:port/articles/2020  # 返回2020年文章列表
http://ip:port/articles/2020/11  # 返回2020年11月份文章列表
http://ip:port/articles/2020/11/123  # 查看ID为123的文章
"""

"""
1、分组匹配内容会传递到函数视图位置参数
2、正则匹配是从左到右，URL匹配从上到下，如果匹配到就返回。
"""