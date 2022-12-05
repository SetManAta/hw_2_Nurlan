from django.urls import path, include

from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('list_item/', views.list_item, name='list_item'),
    path('<int:id>/detail/', views.detail, name='detail'),
]
