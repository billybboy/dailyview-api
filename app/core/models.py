import os
import uuid

from django.db import models
from django.contrib.auth.models import User


def article_image_file_path(instance, filename):
    """Generate file path for new article image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'article', filename)


class Article(models.Model):
    """Article object."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to=article_image_file_path)

    def __str__(self):
        return self.title

