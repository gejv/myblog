from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)
    data = models.IntegerField(null=True, blank=True)


class Department(models.Model):
    title = models.CharField(max_length=16)


class Role(models.Model):
    caption = models.CharField(max_length=16)


class Story(models.Model):
    name = models.CharField(max_length=16)
    content = models.TextField()
    time = models.DateTimeField()
    ip = models.CharField(max_length=64, null=True, blank=True)


class Works(models.Model):
    name = models.CharField(max_length=16)
    src = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    time = models.DateField()


class Image(models.Model):
    url = models.CharField(max_length=255)

# Department.objects.create(title="销售部")

# UserInfo.objects.create(name='we', password='123', age=19)
