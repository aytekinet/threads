from django.contrib import admin
from .models import Thread, Category, Twitter
# Register your models here.@admin.register(Thread)

admin.site.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('thread_title', 'thread_link', 'thread_date', 'category', 'Twitter')
    list_filter = ('category', 'Twitter')
    search_fields = ('thread_title', 'thread_link', 'thread_date', 'category', 'Twitter')

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description', 'category_image')
    search_fields = ('category_name', 'category_description', 'category_image')

admin.site.register(Twitter)
class TwitterAdmin(admin.ModelAdmin):
    list_display = ('twitter_name', 'twitter_link', 'twitter_image')
    search_fields = ('twitter_name', 'twitter_link', 'twitter_image')