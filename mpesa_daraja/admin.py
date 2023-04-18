from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Token)
admin.site.register(PendingTransaction)
admin.site.register(CompleteTransaction)
admin.site.register(Confirmation)