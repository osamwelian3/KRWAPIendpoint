from rest_framework import serializers
from .models import CompleteTransaction as Payment, Confirmation

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=['phone_number']

class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Confirmation
        fields=('TransactionType', 'TransID', 'TransTime', 'TransAmount', 'BusinessShortCode', 'BillRefNumber', 'InvoiceNumber', 'OrgAccountBalance', 'ThirdPartyTransID', 'MSISDN', 'FirstName', 'MiddleName', 'LastName')
