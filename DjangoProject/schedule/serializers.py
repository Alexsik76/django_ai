from .models import Teacher
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    # full_name = serializers.Field(source='full_name')
    discipline = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Teacher
        fields = ['first_name', 'middle_name', 'last_name', 'phone', 'email', 'tg_link', 'full_name', 'discipline']


