from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    # 게시물 관련
    path('', views.main, name="main"),
    path('create', views.create, name="create"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('search/', views.search, name="search"),
    path('search_ajax/', views.search_ajax, name="search_ajax"),
    
    # 좋아요 관련
    path('detail/<int:pk>/like', views.toggle_like, name="toggle_like"),
    
    # 댓글 관련
    path('detail/<int:post_pk>/comment/create', views.comment_create, name="comment_create"),
    path('detail/<int:post_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name="comment_delete"),
]
