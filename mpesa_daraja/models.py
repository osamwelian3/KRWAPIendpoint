from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class PendingTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_reason = models.CharField(max_length=255)
    amount = models.IntegerField()
    phone_number = models.CharField(max_length=13)

    def __str__(self) -> str:
        return f'Transaction of {self.amount} for {self.transaction_reason}'
    
class CompleteTransaction(models.Model):
    merchantRequestID = models.CharField(max_length=255)
    checkoutRequestID = models.CharField(max_length=255)
    resultCode = models.IntegerField()
    resultDesc = models.CharField(max_length=255)
    amount = models.IntegerField()
    mpesaReceiptNumber = models.CharField(max_length=255)
    transactionDate = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=13)

    def __str__(self) -> str:
        return f"Transaction of KES. {self.amount} from {self.phoneNumber}"
    
class Token(models.Model):
    access_token = models.CharField(max_length=255, unique=True)
    expiry = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(0,3599))

    def __str__(self) -> str:
        return f"Access token: {self.access_token}"
    
class Confirmation(models.Model):
    TransactionType = models.CharField(max_length=255)
    TransID = models.CharField(max_length=255)
    TransTime = models.CharField(max_length=255)
    TransAmount = models.CharField(max_length=255)
    BusinessShortCode = models.CharField(max_length=255)
    BillRefNumber = models.CharField(max_length=255)
    InvoiceNumber = models.CharField(max_length=255)
    OrgAccountBalance = models.CharField(max_length=255)
    ThirdPartyTransID = models.CharField(max_length=255)
    MSISDN = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Transaction of {self.TransAmount} from {self.FirstName} {self.LastName}"
    
class Validation(models.Model):
    TransactionType = models.CharField(max_length=255)
    TransID = models.CharField(max_length=255)
    TransTime = models.CharField(max_length=255)
    TransAmount = models.CharField(max_length=255)
    BusinessShortCode = models.CharField(max_length=255)
    BillRefNumber = models.CharField(max_length=255)
    InvoiceNumber = models.CharField(max_length=255)
    OrgAccountBalance = models.CharField(max_length=255)
    ThirdPartyTransID = models.CharField(max_length=255)
    MSISDN = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Transaction of {self.TransAmount} from {self.FirstName} {self.LastName}"
