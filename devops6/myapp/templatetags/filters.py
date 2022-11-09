from django.template import  Library
register = Library()  # 注册过滤器对象
@register.filter   # 通过装饰注册自定义过滤器
def func(n):
    return n / 2
