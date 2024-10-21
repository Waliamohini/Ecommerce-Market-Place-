from django.db import models
from items.models import Item
from django.contrib.auth.models import User


# Create your models here.
class Conversations(models.Model):
    item = models.ForeignKey(Item, related_name = 'conversations', on_delete = models.CASCADE)
    memebers = models.ManyToManyField(User, related_name = 'conversations')
    created_at = models.DateTimeField(auto_now_add= True)
    modified_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ('-modified_at',)
        
class ConvMessages(models.Model):
    conversation = models.ForeignKey(Conversations, related_name = 'messages', on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    User = models.ForeignKey(User, related_name = "messages", on_delete = models.CASCADE)