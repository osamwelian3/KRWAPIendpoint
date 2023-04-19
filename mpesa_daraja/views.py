from django.shortcuts import render
from django import http
from django.views import View
from .models import CompleteTransaction as Payment, Confirmation, Validation
from .serializers import PaymentSerializer, PhoneSerializer, ConfirmationSerializer, ValidationSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .transaction_handler import Transaction
from KRWAPIendpoint.customMixin import PermissionsPerMethodMixin
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import json

# Create your views here.
class PaymentViewSet(PermissionsPerMethodMixin, viewsets.ModelViewSet):
    serializer_class=PaymentSerializer
    queryset=Payment.objects.all()

    @action(detail=False, methods=['post'], serializer_class=PhoneSerializer)
    def pay(self, request, *args, **kwargs):
        if request.method == 'POST':
            phone = request.POST.get('phone_number') if request.POST.get('phone_number') is not None else request.data.get('phone_number')
            amount = request.POST.get('amount') if request.POST.get('amount') is not None else request.data.get('amount')
            accountReference = request.POST.get('account_reference') if request.POST.get('account_reference') is not None else request.data.get('account_reference')
            transactionDesc = request.POST.get('transaction_description') if request.POST.get('transaction_description') is not None else request.data.get('transaction_description')
            transaction = Transaction()
            tr = transaction.stk_push(phone=phone, amount=int(amount), accountReference=accountReference, transactionDesc=transactionDesc)
            if 'errorMessage' in tr:
                return Response({'error': tr['errorMessage']},status=400)
            if 'ResponseCode' in tr:
                if tr['ResponseCode'] == '0':
                    validation = transaction.query_transaction(tr['CheckoutRequestID'])
                    print(validation)
                    while 'errorMessage' in validation:
                        validate = transaction.query_transaction(tr['CheckoutRequestID'])
                        if 'ResultDesc' in validate:
                            if validate['ResultDesc'] == "The initiator information is invalid.":
                                message = "Something went wrong"
                                return Response({'error': message}, status=400)
                            if validate['ResultDesc'] == "DS timeout user cannot be reached":
                                message = "Your phone cannot be reached to initiate transaction"
                                return Response({'error': message}, status=400)
                            if validate['ResultDesc'] == "Request cancelled by user":
                                message = "You took too long or cancelled the PIN request for the transaction Please try again"
                                return Response({'error': message}, status=400)
                            if validate['ResultDesc'] == "The service request is processed successfully.":
                                message = "Yey... Payment went through"
                                return Response({'success': message})
                            
            return Response({'error': 'Something went wrong'})
        return Response({'error': 'Something went wrong'})

    @authentication_classes([])
    @permission_classes((AllowAny, ))
    @action(detail=False, methods=['post', 'get'])
    def callback(self, request, *args, **kwargs):
        if request.method == 'POST':
            merchantRequestID = request.data.get('Body').get('stkCallback').get('MerchantRequestID')
            checkoutRequestID = request.data.get('Body').get('stkCallback').get('CheckoutRequestID')
            resultCode = request.data.get('Body').get('stkCallback').get('ResultCode')
            transactionDate = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[2].get('Value')
            transaction_id = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[1].get('Value')
            phone_number = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[3].get('Value')
            amount = request.data.get('Body').get('stkCallback').get('CallbackMetadata').get('Item')[0].get('Value')
            status = request.data.get('Body').get('stkCallback').get('ResultDesc')
            payment = Payment.objects.create(merchantRequestID=merchantRequestID, checkoutRequestID=checkoutRequestID, resultCode=resultCode, transactionDate=transactionDate, mpesaReceiptNumber=transaction_id, phoneNumber=phone_number, amount=amount, resultDesc=status)
            payment.save()
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return Response(dict(context))
    
    @authentication_classes([])
    @permission_classes((AllowAny, ))
    @action(detail=False, methods=['post', 'get'], serializer_class=ConfirmationSerializer)
    def confirmation(self, request, *args, **kwargs):
        if request.method == 'POST':
            TransactionType = request.data.get('TransactionType')
            TransID = request.data.get('TransID')
            TransTime = request.data.get('TransTime')
            TransAmount = request.data.get('TransAmount')
            BusinessShortCode = request.data.get('BusinessShortCode')
            BillRefNumber = request.data.get('BillRefNumber')
            InvoiceNumber = request.data.get('InvoiceNumber')
            OrgAccountBalance = request.data.get('OrgAccountBalance')
            ThirdPartyTransID = request.data.get('ThirdPartyTransID')
            Msisdn = request.data.get('MSISDN')
            FirstName = request.data.get('FirstName')
            MiddleName = request.data.get('MiddleName')
            LastName = request.data.get('LastName')

            confirmation = Confirmation.objects.create(TransactionType=TransactionType, TransID=TransID, TransTime=TransTime, TransAmount=TransAmount, 
                                                       BusinessShortCode=BusinessShortCode, BillRefNumber=BillRefNumber, InvoiceNumber=InvoiceNumber, 
                                                       OrgAccountBalance=OrgAccountBalance, ThirdPartyTransID=ThirdPartyTransID, MSISDN=Msisdn, FirstName=FirstName, 
                                                       MiddleName=MiddleName, LastName=LastName)
            confirmation.save()
            
            context = {
                "ResultCode": 0,
                "ResultDesc": "Accepted"
            }
            return Response(dict(context))
        return Response(ConfirmationSerializer(Confirmation.objects.all(), many=True).data)
    
    @authentication_classes([])
    @permission_classes((AllowAny, ))
    @action(detail=False, methods=['post', 'get'], serializer_class=ValidationSerializer)
    def validation(self, request, *args, **kwargs):
        if request.method == 'POST':
            TransactionType = request.data.get('TransactionType')
            TransID = request.data.get('TransID')
            TransTime = request.data.get('TransTime')
            TransAmount = request.data.get('TransAmount')
            BusinessShortCode = request.data.get('BusinessShortCode')
            BillRefNumber = request.data.get('BillRefNumber')
            InvoiceNumber = request.data.get('InvoiceNumber')
            OrgAccountBalance = request.data.get('OrgAccountBalance')
            ThirdPartyTransID = request.data.get('ThirdPartyTransID')
            Msisdn = request.data.get('MSISDN')
            FirstName = request.data.get('FirstName')
            MiddleName = request.data.get('MiddleName')
            LastName = request.data.get('LastName')

            confirmation = Validation.objects.create(TransactionType=TransactionType, TransID=TransID, TransTime=TransTime, TransAmount=TransAmount, 
                                                       BusinessShortCode=BusinessShortCode, BillRefNumber=BillRefNumber, InvoiceNumber=InvoiceNumber, 
                                                       OrgAccountBalance=OrgAccountBalance, ThirdPartyTransID=ThirdPartyTransID, MSISDN=Msisdn, FirstName=FirstName, 
                                                       MiddleName=MiddleName, LastName=LastName)
            confirmation.save()
            
            context = {
                "ResultCode": 0,
                "ResultDesc": "Accepted"
            }
            return Response(dict(context))
        return Response(ConfirmationSerializer(Confirmation.objects.all(), many=True).data)
    
    @authentication_classes([])
    @permission_classes((AllowAny, ))
    @action(detail=False, methods=['post', 'get'])
    def registerurl(self, request, *args, **kwargs):
        data = Transaction().registerConfirmationurls()
        return Response(data)
