from django.db import models

# Create your models here.


class Robots(models.Model):
    objects = None
    nomi = models.CharField(max_length=200)
    rangi = models.CharField(max_length=200)
    kattaligi = models.CharField(max_length=200)
    price = models.IntegerField()
    davlati = models.CharField(max_length=200)

    def __str__(self):
        return self.nomi
