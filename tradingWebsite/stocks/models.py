from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money_left = models.FloatField()

    def __str__(self):
        return self.user.username


class Stock(models.Model):
    name = models.CharField(max_length=25)
    shares = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
