from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_ai.schedule.models import Teacher, AcademicDiscipline, ImageModel
from django_ai.schedule.serializers import TeacherSerializer, DisciplineSerializer, ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('last_name')
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = AcademicDiscipline.objects.all().order_by('name')
    serializer_class = DisciplineSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)


# class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ImageModel.objects.all()
#     serializer_class = ImageSerializer
@api_view(['POST'])
def images_post(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','DELETE'])
# def image_postl(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         image = ImageModel.objects.get(pk=pk)
#     except ImageModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ImageSerializer(image)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ImageSerializer(image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)