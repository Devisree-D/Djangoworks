from django.db import models

# Create your models here.
class Studentreg(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=120)
    phone=models.IntegerField()
    username=models.CharField(max_length=120,unique=True)
    password=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Studentlog(models.Model):
    username=models.CharField(max_length=120, unique=True )
    password=models.CharField(max_length=120)

    def __str__(self):
        return self.username
