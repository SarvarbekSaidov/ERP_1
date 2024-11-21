from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Lesson, Instructor
from .serializers import LessonSerializer, InstructorSerializer
from .permissions import IsInstructor

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]   

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [IsAuthenticated, IsInstructor]   
