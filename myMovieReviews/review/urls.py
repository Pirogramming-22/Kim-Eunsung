from django.urls import path
from .views import *

app_name = 'review'

urlpatterns = [
    
    # 글쓰기
    path('create', review_create, name='review_create'),

    # 리스트
    path('', review_list, name='review_list'),
    path('list', review_list, name='review_list'),

    # 디테일
    path('detail/<int:pk>', review_detail, name='review_detail'),
    
    # 업데이트
    path('update/<int:pk>', review_update, name='review_update'),
    
    # 삭제
    path('delete/<int:pk>', review_delete, name='review_delete')
]