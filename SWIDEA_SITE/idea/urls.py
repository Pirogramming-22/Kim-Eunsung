from django.urls import path
from idea import views

app_name = 'idea'

urlpatterns = [
    path('', views.main, name='main'),
    path('list', views.list, name='idea_list'),
    path('create', views.create, name='idea_create'),
    path('detail/<int:pk>', views.detail, name='idea_detail'),
    path('update/<int:pk>', views.update, name='idea_update'),
    path('delete/<int:pk>', views.delete, name='idea_delete'),
    
    path('<int:pk>/zzim', views.zzimToggle, name='idea_zzimToggle'),
    path('<int:pk>/interestup', views.interestup, name='idea_interestup'),
    path('<int:pk>/interestdown', views.interestdown, name='idea_interestdown'),
]