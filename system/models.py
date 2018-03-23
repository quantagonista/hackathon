from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(User):

    class Meta:
        proxy = True

class Profession(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(Person)

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    profession = models.ForeignKey(Profession)
    # status = mode
