from django.urls import path, include

from . import views

urlpatterns = [
    path('greetings/', views.index, name='index'),
    path('greetings/list_item', views.list_item, name='list_item'),
    path('greetings/<int:id>/detail/', views.detail, name='detail'),
]
