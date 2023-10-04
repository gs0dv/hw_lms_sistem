from django.urls import path
from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDeleteAPIView, PaymentListViewSet, PaymentCreateViewSet

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
                  path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson-delete'),

                  path('payments/', PaymentListViewSet.as_view(), name='payments-list'),
                  path('payments/create/', PaymentCreateViewSet.as_view(), name='payment-create'),

              ] + router.urls
