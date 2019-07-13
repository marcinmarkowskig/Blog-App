from django.db.models.signals import post_save #import sygnaly, ktory nastapi po savie usera
from django.contrib.auth.models import User
from django.dispatch import receiver#to jest chyba jakis decorator
from .models import Profile

#automatyczne tworzenie profilu, gdy tworzony jest user; dzieki temu nie trzeba wchodzic zawsze do admina i tworzyc profilu dla kazdego nowego usera
@receiver(post_save, sender=User)#kiedy user jest zapisywany wyslij sygnal post_save
def create_profile(sender, instance, created, **kwargs):#wszyskie parametry w nawiasie pochodza od post_save z gory
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)#kiedy user jest zapisywany wyslij sygnal post_save
def save_profile(sender, instance, **kwargs):#wszyskie parametry w nawiasie pochodza od post_save z gory
    instance.profile.save()
