from rest_framework import permissions, viewsets

from .models import Teacher, AcademicDiscipline
from .serializers import TeacherSerializer, DisciplineSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('last_name')
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = AcademicDiscipline.objects.all().order_by('name')
    serializer_class = DisciplineSerializer
    # permission_classes = [permissions.IsAuthenticated]
