from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书籍名称")
    price = models.IntegerField(verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版日期")

    class Meta:
        db_table = "Book"
        verbose_name = "书"
        verbose_name_plural = "书"

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")
    addr = models.CharField(max_length=32, verbose_name="地址")

    class Meta:
        db_table = "Publish"
        verbose_name = "出版"
        verbose_name_plural = "出版"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")
    age = models.IntegerField(verbose_name="年龄")

    class Meta:
        db_table = "Author"
        verbose_name = "作者"
        verbose_name_plural = "作者"

    def __str__(self):
        return self.name
