from django.urls import path, include, re_path
from myapp import views

urlpatterns = [
    re_path('index/$', views.index),
    re_path('register/$', views.user_add),
    re_path('api/$', views.api),
    re_path('onetoone/$', views.onetoone),
    re_path('^app/$', views.app),
    re_path('^project/$', views.project),
    re_path('^app_add/$', views.app_add),
    re_path('^server/$', views.server),
    re_path('project_app_server/$', views.project_app_server),
    re_path('^login/$', views.login),
    re_path('^logout/$', views.logout),
]
