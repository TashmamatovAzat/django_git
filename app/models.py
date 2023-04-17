from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
