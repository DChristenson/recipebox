from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    #user is for auth
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Recipe(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    desc = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title}'