from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TeacherViewSet, DisciplineViewSet, ImageViewSet, images_post

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'disciplines', DisciplineViewSet)
router.register(r'process_photo', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls',
    #                           namespace='rest_framework')),

    # path('image_post/', images_post),
    # path('process_photo/', ImageList.as_view()),
    # path('process_photo/', ImageList.as_view()),
    # path('process_photo/<int:pk>', ImageDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)