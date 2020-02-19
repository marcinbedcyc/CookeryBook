from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(
        default='default_user_pic.png', upload_to='profile_imgs')

    def __str__(self):
        return f"{self.user.username}'s additional info"

    def save(self, *args, **kwargs):
        super().save()
        maxsize = (256, 256)
        img = Image.open(self.profile_img.path)
        if img.height > 256 or img.width > 256:
            img.thumbnail(maxsize)
            img.save(self.profile_img.path)
