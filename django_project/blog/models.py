from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):#po zapisaniu posta/utworzeniu posta nastepuje przekierowanie do wygladu tego posta, a nie powrot do strony glownej; zwizane z redirect
        return reverse('post-detail', kwargs={'pk': self.pk})
