from django.db import models

# Create your models here.
class Todo(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = 'IN_PROGRESS'
        COMPLETED = 'COMPLETED'
    
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    status = models.CharField(choices=Status.choices, default=Status.IN_PROGRESS, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
