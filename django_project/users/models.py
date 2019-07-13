from django.db import models
from django.contrib.auth.models import User
from PIL import Image #Pillow - do resize image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one relationship with User model, co się stanie, jeśli zostanie usunięty user - CASCADE - zostanie usunięcty rózwnież profil
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')#zostanie utworzone directory profile_pics

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
