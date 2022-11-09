from django.db import models

# Create your models here.
from django.db import models


# 用户表
class User(models.Model):
    user = models.CharField(max_length=30, verbose_name="用户")
    name = models.CharField(max_length=30, verbose_name="姓名")
    sex = models.CharField(max_length=10, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    label = models.CharField(max_length=100, verbose_name="标签")
    test = models.CharField(null=True, blank=True, default="123", verbose_name="测试字段", max_length=30)

    class Meta:
        app_label = "myapp"
        db_table = "user"
        verbose_name = "用户表"  # 显示的名字
        verbose_name_plural = "用户表"  # 将用户表s改为用户表

    def __str__(self):
        return self.name  # 返回字段值


# 身份证表
class IdCard(models.Model):
    number = models.CharField(max_length=30, verbose_name="身份证号")
    address = models.CharField(max_length=100, verbose_name="住址")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "idcard"
        verbose_name_plural = "身份证表"

    def __str__(self):
        return self.number  # 返回字段值


# 应用表
class Project(models.Model):
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=100)
    datatime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "project"
        verbose_name_plural = "项目"

    def __str__(self):
        return self.name


# 应用表
class App(models.Model):
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=100, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # 定义一对多的模型关系

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app'

    verbose_name_plural = '应用'


# 服务器表
class Server(models.Model):
    hostname = models.CharField(max_length=30)
    ip = models.GenericIPAddressField()
    describe = models.CharField(max_length=100)
    datatime = models.DateTimeField(auto_now_add=True)
    app = models.ManyToManyField(App)

    class Meta:
        db_table = "server"
        verbose_name_plural = "服务器"

    def __str__(self):
        return self.hostname
