from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    college = models.CharField(max_length=100)
    leetcode_id = models.CharField(max_length=50)

    def __str__(self):
        return self.username
