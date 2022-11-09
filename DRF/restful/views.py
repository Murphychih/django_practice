from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Book
from rest_framework.generics import GenericAPIView
import time

# from restful.models import Book


# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=4)
#     price = serializers.IntegerField()
#     date = serializers.DateField(source='pub_date')
#
#     def create(self, validated_data):
#         ##添加数据逻辑 解耦
#         new_book = Book.objects.create(**validated_data)
#         return new_book
#
#     def update(self, instance, validate_date):
#         Book.objects.filter(pk=instance.pk).update(**self.validated_data)
#         updated_book = Book.objects.get(pk=instance.pk)
#         return updated_book


# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source="pub_date")
#     class Meta:
#         model = Book
#         # fields = ["title", "price"]
#         fields = "__all__"
#         # exclude = ["pub_date"] fields exclude不能同时兼得


'''
                    基于APIView的接口实现
'''

# class BookView(APIView):
#
#     def get(self, request):
#         book_list = Book.objects.all()
#         print(book_list)
#         # 构建序列化对象： BookSerializers(instance=, data=) instance是序列化 data是反序列化
#         Serializer = BookSerializers(instance=book_list, many=True)
#         print("query_params: ", request.query_params)
#         return Response(Serializer.data)
#
#     def post(self, request):
#         print("post.query_params", request.query_params)
#         print("post.data", request.data)
#         serializer = BookSerializers(data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 返回布尔值 serializer.validated_data serializer.errors 存的是错误的键值对
#             # Book.objects.create(title=obj['title'], price=obj['price'], pub_date=obj['pub_date'])
#             # new_book = Book.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.validated_data)
#         else:
#             # 校验失败
#             return Response(serializer.errors)
#         # print("serializers.data", serializer.validated_data)
#         # return HttpResponse("post")
#
#
# class BookDetailView(APIView):
#
#     def delete(self, request, book_id):
#         Book.objects.get(pk=book_id).delete()
#         return Response()
#
#     def get(self, request, book_id):
#         book = Book.objects.get(pk=book_id)
#         # star_time = time.time()
#         serializer = BookSerializers(instance=book, many=False)
#         # print("duration %s" % (star_time - time.time()))
#         return Response(serializer.data)
#
#     def put(self, request, book_id):
#         update_book = Book.objects.get(pk=book_id)
#         # 不传instance就会重新建立一条数据，而不会更新
#         serializer = BookSerializers(instance=update_book, data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 返回布尔值 serializer.validated_data serializer.errors 存的是错误的键值对
#             # 更新逻辑
#             # Book.objects.filter(pk=book_id).update(**serializer.validated_data)
#             # updated_book = Book.objects.get(pk=book_id)
#             # serializer.instance = updated_book
#             serializer.save()
#             return Response(serializer.data)  # 老数据
#
#         else:
#             # 校验失败
#             return Response(serializer.errors)

'''
                    基于GenericAPIView的接口实现
'''

# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source="pub_date")
#
#     class Meta:
#         model = Book
#         fields = "__all__"
#
#
# class BookView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self, request):
#         # serializer = BookSerializers(instance=self.get_queryset(), many=True)
#         # serializer = self.get_serializer_class()(instance=self.get_queryset(), many=True)
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         # 上两种写法相同
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data, many=False)
#         # serializer = BookSerializers(data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 返回布尔值 serializer.validated_data serializer.errors 存的是错误的键值对
#             serializer.save()
#             return Response(serializer.validated_data)
#         else:
#             # 校验失败
#             return Response(serializer.errors)
#
#
# class BookDetailView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def delete(self, request, pk):
#         self.get_object().delete()
#         return Response()
#
#     def get(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 返回布尔值 serializer.validated_data serializer.errors 存的是错误的键值对
#             serializer.save()
#             return Response(serializer.data)  # 老数据
#         else:
#             # 校验失败
#             return Response(serializer.errors)


"""
                基于mixin混合类  多继承
"""

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin

# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source="pub_date")
#
#     class Meta:
#         model = Book
#         fields = "__all__"
#
#
# class BookView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)


"""
                再封装
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#
# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source="pub_date")
#
#     class Meta:
#         model = Book
#         fields = "__all__"
#
#
# class BookView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


"""
                再再封装（离谱  ViewSet:重新构建分发机制
"""

from rest_framework.viewsets import ViewSet

# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source="pub_date")
#
#     class Meta:
#         model = Book
#         fields = "__all__"
#
#
# class BookView(ViewSet):
#
#     def get_all(self, request):
#         return Response("查看所有资源")
#
#     def add_object(self, request):
#         return Response("添加资源")
#
#     def get_object(self, request, pk):
#         return Response("查看单一资源")
#
#     def update_object(self, request, pk):
#         return Response("更新单一资源")
#
#     def delete_object(self, request, pk):
#         return Response("删除单一资源")


"""
                                    Final版
"""

from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin



class BookSerializers(serializers.ModelSerializer):
    date = serializers.DateField(source="pub_date")

    class Meta:
        model = Book
        fields = "__all__"

#
# class BookView(GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
#     serializer_class = BookSerializers
#     queryset = Book.objects.all()


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

"""
                Token 认证
                
            首先在setting里面添加 
"""