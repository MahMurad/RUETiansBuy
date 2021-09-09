from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    price = models.FloatField(null=True)
    new = models.BooleanField(default=True)
    description = models.TextField()
    photo = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)
    contact_no = models.CharField(max_length=14, unique=True)


#Class User(models.Model):
#    id = models.AutoField(primary_key = True)
#    seller = models.CharField(max_length=30, unique=True)
#    contact_no = models.CharField(max_length=14, unique=True)
#    photo = models.ImageField()
