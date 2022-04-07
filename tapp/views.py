from django.shortcuts import render
from .models import Thread, Category, Twitter

# Create your views here.

def index(request):
    #bookmark_list = Bookmarks.objects.all().order_by('-date')[:9]
    categories = Category.objects.all()
    total_links = Thread.objects.count()
    #categoryname = Category.objects.all()
    #courses = Course.objects.all().order_by('-date') 
    #total_links = Bookmarks and addSite .objects.count()
    #siteAdd =   addSite.objects.all()

    
    

    context = {
        'categories': categories,
        'total_links': total_links,

    }

    return render(request, 'index.html', context)


def thread_detail (request, category_slug):
    categories = Category.objects.get(category_slug=category_slug)
    twitters = Twitter.objects.all().filter()
    threads = Thread.objects.all().filter(category=categories)
    context = {
        'categories': categories,
        'threads': threads,
        'twitters': twitters,
    }
    return render(request, 'threads.html', context)
