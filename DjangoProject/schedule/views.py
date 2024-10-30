from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Teacher
from .serializers import TeacherSerializer



class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Teacher.objects.all().order_by('last_name')
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


