from django.contrib import admin

from .models import Conversations, ConvMessages

admin.site.register(Conversations)
admin.site.register(ConvMessages)
