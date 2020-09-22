from django.db import models
from PIL import Image

# Create your models here.


class Imgcompress(models.Model):
    img = models.ImageField(
        upload_to="imgupload/compress/", blank=True)

    def save(self):
        super().save()  # saving image first

        image = Image.open(self.img.path)  # Open image using self

        if image.height > 300 or image.width > 300:
            new_img = (300, 300)
            image.thumbnail(new_img)
            image.save(self.img.path)
