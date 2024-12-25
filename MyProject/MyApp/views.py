from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.core.files.base import ContentFile
from .models import UploadedFile


class FileUploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'upload.html')

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']

        file_instance = UploadedFile()
        file_instance.original_file.save(uploaded_file.name, ContentFile(uploaded_file.read()))
        file_instance.save()

        return JsonResponse({
            'message': 'Файл успешно загружен',
            'original_file': file_instance.original_file.url,
            'thumbnail': file_instance.thumbnail.url if file_instance.thumbnail else None,
        })
