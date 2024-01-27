from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField(max_length=700,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField(max_length=2000,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")

    def __str__(self):
        return self.name

class Stakeholder(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 50, null = False)
    f_name = models.CharField(max_length = 50, null = False)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

    def __str__(self):
        return self.f_name
    
class News(models.Model):
    title = models.CharField(max_length = 50,null = False)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length = 500, null= False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
        