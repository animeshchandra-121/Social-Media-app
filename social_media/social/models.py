from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank= True, related_name= "likes")
    dislikes = models.ManyToManyField(User, blank= True, related_name= "dislike")

class Comments(models.Model):
    post = models.ForeignKey('Post', on_delete= models.CASCADE)
    users = models.ForeignKey(User , on_delete= models.CASCADE, null= True, blank= True)
    comments = models.TextField()
    created_on = models.DateTimeField(default= timezone.now)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key= True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length= 200, blank= True, null= True)
    bio = models.TextField(max_length= 500, blank= True, null= True)
    birth_date = models.DateField(null= True, blank= True)
    location = models.CharField(max_length= 100, blank= True, null= True)
    picture = models.ImageField(upload_to='uploads/', default='uploads/default.png', blank= True)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
