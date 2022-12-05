from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item, Purchase


def index(request):
    items_list = Item.objects.all()
    context = {
        'items_list':items_list
    }
    return render(request,'index.html',context)

def list_item(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'list_item.html', context)

def detail(request, id):
    items = get_object_or_404(Item, id=id)
    context = {
        'items' : items
    }
    return render(request, 'detail_item.html', context)
