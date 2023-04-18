# from django.db import models
# from django.conf import settings

# User = settings.AUTH_USER_MODEL

# # Create your models here.
# class Member(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     membership_code = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     other_names = models.CharField(max_length=255)
#     GENDER = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Other', 'Other')
#     )
#     gender = models.CharField(choices=GENDER, max_length=7)
#     MARITAL_STATUS = (
#         ('Single', 'Single'),
#         ('Married', 'Married'),
#         ('Seperated', 'Seperated'),
#         ('Divorced', 'Divorced')
#     )
#     marital_status = models.CharField(choices=MARITAL_STATUS, max_length=10)
#     id_or_passport = models.CharField(max_length=10)
#     occupation = models.CharField(max_length=255)
#     place_of_work = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.first_name} {self.last_name}"


# class Residence(models.Model):
#     member = models.OneToOneField(Member, on_delete=models.CASCADE)
#     county = models.CharField(max_length=255)
#     constituency = models.CharField(max_length=255)
#     ward = models.CharField(max_length=255)
#     estate = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.estate}"
    
# class Contact(models.Model):
#     member = models.OneToOneField(Member, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=13)
#     alternative_phone = models.CharField(max_length=13)
#     postal_address = models.CharField(max_length=10)
#     postal_code = models.CharField(max_length=10)
#     postal_town = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.phone}"

    
 