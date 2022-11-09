from django.contrib import admin

# Register your models here.
from myapp import models

admin.site.register(models.User) #注册User表到后台
admin.site.register(models.Project) #注册Project表到后台
admin.site.register(models.App) #注册App表到后台
admin.site.register(models.Server) #注册Server表到后台
