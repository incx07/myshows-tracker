from django.db import models
from django.conf import settings


class SerialLater(models.Model):
    user_link = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    myshows_id = models.PositiveSmallIntegerField(default=0)
    title_eng = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title_eng


class SerialComplete(models.Model):
    user_link = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    myshows_id = models.PositiveSmallIntegerField(default=0)
    title_eng = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField(default=0)
    rating = models.CharField(max_length=50, default='No')

    def __str__(self):
        return self.title_eng
