from django.urls import path
from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDeleteAPIView, PaymentViewSet

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
                  path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson-delete'),

              ] + router.urls
