from django.urls import path
from . import views

urlpatterns = [
  path('', views.index,name="index"),
  path('category/<slug:category_slug>', views.thread_detail, name="threads_by_category"),
  
  ]