from django.urls import path
from .views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file_upload'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
]