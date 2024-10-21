from django.shortcuts import render, get_object_or_404, redirect

from items.models import Item
from .models import Conversations
from .forms import ConversationMessage


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.User == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversations.objects.filter(item = item).filter(members__in = [request.user.id])
    
    if conversations:
        pass #redirect to the converesations form
    
    
    if request.method == 'POST':
        form = ConversationMessage(request.POST)
        
        if form.is_valid():
            conversation = Conversations.objects.create(item = item)
            conversation.members.add(request.user)
            conversation.members.add(item.User)
            conversation.save()
            
            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.User = request.user
            conversation_message.save()
            return redirect("items:details", pk=item_pk)
        else:
            form = ConversationMessage()
    return render(request, "conversations/new.html", {'form' : form})