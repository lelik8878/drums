from django.contrib import admin

from .models import Participant, Payment, Statement

admin.site.register(Participant)
admin.site.register(Payment)
admin.site.register(Statement)
