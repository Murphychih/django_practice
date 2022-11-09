from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

from restful import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('book', views.BookView, basename='book')

urlpatterns = [
    # path("api/", views.BookView.as_view({"get": "list", "post": "create"})),
    # # re_path("^api/(\d+)", views.BookDetailView.as_view()),
    # re_path("^api/(?P<pk>\d+)", views.BookView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))

]

urlpatterns += router.urls