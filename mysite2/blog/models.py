from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Sport(models.Model):
    class Meta:
        db_table = "시설명"
    name = models.CharField(max_length=70, default='')

class SportComplex(models.Model):
    class Meta:
        db_table = "공공체육시설"
    name = models.ManyToManyField(Sport, related_name ='mysite2')
    category = models.CharField(max_length=70, default='')
    city = models.CharField(max_length=70, default='')
    detail = models.CharField(max_length=70, default='')
    lon = models.CharField(max_length=70, default='')
    lat = models.CharField(max_length=70, default='')
    status = models.CharField(max_length=70, default='')