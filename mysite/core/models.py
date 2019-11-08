from django.db import models


# Create your models here.
class BlogPost(models.Model):
    """This is the blog model"""
    id = models.AutoField(primary_key=True)
    title = models.fields.CharField(max_length=128)
    post=models.fields.CharField(max_length=1024)
    created_on=models.DateTimeField(auto_now_add=True)
    edited_on=models.DateTimeField(auto_now=True)
