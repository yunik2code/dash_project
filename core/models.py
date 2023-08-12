from typing import Any
from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    pseudo_name=models.CharField(max_length=15)
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_time=models.DateTimeField(auto_created=True,auto_now=True)
    post_id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    post_field=models.CharField(max_length=40,blank=True)

    def __repr__(self) -> str:
        return self.pseudo_name

class History(models.Model):
    session_key=models.CharField(max_length=200,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return self.id
    
class Like(models.Model):
    session_key=models.CharField(max_length=200,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return self.session_key

class DisLike(models.Model):
    session_key=models.CharField(max_length=200,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return self.session_key

class Views(models.Model):
    session_key=models.CharField(max_length=200,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()
    status=models.CharField(max_length=20)

    def __repr__(self) -> str:
        return self.comment