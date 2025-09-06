from django.db import models

# I dont wanna use Users here I think
from django.contrib.auth.models import User


class Result(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField

    def __str__(self):
        return f"Result from {self.worker.username} at {self.created_at}"
