from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length= 100 )
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length= 100 )

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length= 70 )
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length= 200 ,blank= True)
    category = models.ForeignKey(Category)#分类会有个分类ID
    tags = models.ManyToManyField(Tag,blank=True)#多对多需要额外建立多一张ID关联表
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
# Create your models here.
