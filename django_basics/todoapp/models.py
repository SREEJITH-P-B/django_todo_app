from django.db import models
class detailss(models.Model):
    text=models.CharField(max_length=100)
    completed=models.BooleanField()

# Create your models here.
