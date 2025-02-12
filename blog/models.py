from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 288 or img.width > 370:
            output_size = (288, 370)
            img.thumbnail(output_size)
            img.save(self.image.path)


