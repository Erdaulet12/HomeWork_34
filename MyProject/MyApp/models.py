from django.db import models
from django.core.files.storage import FileSystemStorage
from PIL import Image
import os

# Create your models here.

file_storage = FileSystemStorage(location='media/uploads')


class UploadedFile(models.Model):
    original_file = models.FileField(storage=file_storage, upload_to='originals/')
    thumbnail = models.ImageField(storage=file_storage, upload_to='thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.original_file:
            self.generate_thumbnail()

    def generate_thumbnail(self):
        original_path = self.original_file.path
        thumb_path = os.path.join('media/uploads/thumbnails', os.path.basename(original_path))

        with Image.open(original_path) as img:
            img.thumbnail((200, 200))
            img.save(thumb_path)

        self.thumbnail.name = thumb_path.replace('media/uploads/', '')
        super().save(update_fields=['thumbnail'])
