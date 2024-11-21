from rest_framework import serializers
from .models import Lesson, Instructor

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'user', 'bio', 'lessons']
