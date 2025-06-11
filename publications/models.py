from django.db import models
from ckeditor.fields import RichTextField

class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    issue = models.CharField(max_length=50)  # Masalan: "2025/1"
    cover_image = models.ImageField(upload_to='covers/')
    published_at = models.DateField()

    def __str__(self):
        return f"{self.issue} - {self.title}"