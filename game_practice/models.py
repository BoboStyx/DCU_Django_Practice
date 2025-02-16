from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=150)

    def __str__(self):
        return self.platform
    

class Game(models.Model):
    Name = models.CharField(max_length=150)
    Description = models.TextField()
    Price = models.FloatField(default=60)
    Number_In_Stock = models.PositiveIntegerField(default=1)
    Game_Platform = models.ManyToManyField(Platform)
    Game_Genre = models.TextField(default='action')

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ManyToManyField(Game, blank=True)

    def __str__(self):
        return f"Cart of {self.user.username}"