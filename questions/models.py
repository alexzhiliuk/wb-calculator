from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    user = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email}: {self.text[:20]}..."
