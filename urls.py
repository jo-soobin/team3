from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('sport', views.sport, name='sport'),
    path('minwon', views.minwon, name='minwon'),
]