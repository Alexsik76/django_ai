from django.urls import include, path
from rest_framework import routers

from .views import TeacherViewSet, DisciplineViewSet

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'disciplines', DisciplineViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]