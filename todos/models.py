from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.CharField(max_length=35)
    content = models.CharField(max_length=50)
    dueTo = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    