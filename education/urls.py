from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, InstructorViewSet

router = DefaultRouter()
router.register(r'lessons', LessonViewSet)
router.register(r'instructors', InstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
