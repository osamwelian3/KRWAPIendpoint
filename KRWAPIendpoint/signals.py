from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from rest_framework.authtoken.models import Token 


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def token_generator(sender, instance=None, created=False, **kwargs):
    print('signal received')
    if created:
        Token.objects.create(user=instance)
        print('token created')