from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL

# Create your models here.
# class PendingTransaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     transaction_reason = models.CharField(max_length=255)
#     amount = models.IntegerField()
#     phone_number = models.CharField(max_length=13)

#     def __str__(self) -> str:
#         return f'Transaction of {self.amount} for {self.transaction_reason}'
