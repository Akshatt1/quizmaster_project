from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class quiz(models.Model):
              
              title = models.CharField(max_length=50)
              name = models.CharField(max_length=25)
              data = models.TextField()
              photo = models.ImageField(upload_to='photos/',blank=True,null=True)
              posted_at = models.DateTimeField(auto_now_add=True)   
                 
              
       
