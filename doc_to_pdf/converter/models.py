from django.db import models

class UploadedDocument(models.Model):
    name = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
