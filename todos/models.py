from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.UUIDField()
    content = models.CharField(max_length=50)
    dueTo = models.DateTimeField()
    createdAt = models.DateTimeField()
    done = models.BooleanField(default=False)
    