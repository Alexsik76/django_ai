from django_ai.schedule.models import Teacher, AcademicDiscipline, ImageModel
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    discipline = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'phone',
                  'email', 'tg_link', 'full_name', 'discipline']


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='full_name'
    )

    class Meta:
        model = AcademicDiscipline
        fields = ['id', 'name', 'teacher']

class ImageSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, default="Image")
    description = serializers.CharField(required=False, default="uploaded image")
    created_at = serializers.DateTimeField(required=False)
    image_url = serializers.ImageField(required=False)
    def validate(self, attrs):
        return attrs
    class Meta:
        model = ImageModel
        fields = ["title", "description", 'created_at', "image_url"]
