from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=13)
    profile_form_filled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"User profile for {self.user.username}"
