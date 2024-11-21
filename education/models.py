from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    lessons = models.ManyToManyField(Lesson, related_name='instructors')

    def __str__(self):
        return self.user.username
