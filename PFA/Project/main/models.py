from django.db import models

# Create your models here.
class Image(models.Model):
 image = models.ImageField(upload_to="myimage")
 tags = models.CharField(max_length=100)
 date = models.DateTimeField(auto_now=True)

