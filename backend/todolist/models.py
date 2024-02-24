from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)