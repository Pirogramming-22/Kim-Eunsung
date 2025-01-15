from django.urls import path
from devtool import views

app_name = 'devtool'

urlpatterns = [
    path('devtool/list', views.list, name='devtool_list'),
    path('devtool/create', views.create, name='devtool_create'),
    path('devtool/detail/<int:pk>', views.detail, name='devtool_detail'),
    path('devtool/delete/<int:pk>', views.delete, name='devtool_delete'),
    path('devtool/update/<int:pk>', views.update, name='devtool_update'),
]