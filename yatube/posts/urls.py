from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Посты, отфильтрованные по группам.
    path('group/', views.group_posts)
]