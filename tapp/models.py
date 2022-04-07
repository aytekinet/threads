from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    category_description = models.TextField( max_length=300)
    category_icon_code = models.CharField(max_length=200, help_text='ex: fa fa-code , look fontawesome 4.7 icons', default='fa fa-code')
    

    def __str__(self):
        return self.category_name

class Twitter(models.Model):
    twitter_name = models.CharField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    twitter_image = models.ImageField(upload_to='twitter_image', blank=True)
 
    def __str__(self):
        return self.twitter_name


class Thread(models.Model):
    thread_title = models.CharField(max_length=200)
    thread_link = models.URLField(max_length=200)
    thread_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, blank=True, default='All')
    twitter = models.ForeignKey('Twitter', on_delete=models.CASCADE)

    def __str__(self):
        return self.thread_title
    

