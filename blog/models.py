from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #User is a separate table. 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete, if user is deleted then the post is deleted as well
    
    def __str__(self):
        return self.title
