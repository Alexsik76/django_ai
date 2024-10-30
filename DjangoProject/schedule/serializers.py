from .models import Teacher, AcademicDiscipline
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    discipline = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'phone', 'email', 'tg_link', 'full_name', 'discipline']

class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='full_name'
    )
    class Meta:
        model = AcademicDiscipline
        fields = ['id', 'name', 'teacher']
