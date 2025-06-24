from django.db import models
import os
from django.conf import settings

def upload_to(instance, filename):

    upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
    os.makedirs(upload_path, exist_ok=True)
    return f"uploads/{filename}"

class Upload(models.Model):
    FILE_TYPES = [
        ('pdf', 'PDF'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]
    file = models.FileField(upload_to=upload_to)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.file_type})"
