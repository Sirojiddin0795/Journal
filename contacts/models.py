from django.db import models

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    map_embed_code = models.TextField(help_text="Iframe code or map embed HTML", blank=True)

    def __str__(self):
        return "Contact Info"
