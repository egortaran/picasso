from rest_framework import views, status
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(views.APIView):
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            process_file.delay(file_serializer.instance.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(views.APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
