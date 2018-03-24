# coding=utf-8
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


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Name")
    email = models.EmailField(max_length=255, verbose_name=u"Email")
    text = models.TextField(verbose_name=u"Message")

GENDER_CHOICES = [
    ['male', u"Мужской"],
    ['female', u"Женский"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    avatar = models.FileField(verbose_name=u"Аватар", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Дата рождения")
    gender = models.CharField(max_length=10, verbose_name=u"Пол", choices=GENDER_CHOICES, default="male")
    profession = models.CharField(max_length=20, verbose_name=u"Профессия", default="none")