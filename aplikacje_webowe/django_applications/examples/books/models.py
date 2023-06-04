from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='books/%Y/%m/%d/', blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return f"{self.title} ({self.author})"
