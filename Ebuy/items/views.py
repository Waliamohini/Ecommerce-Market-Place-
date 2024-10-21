from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Categories
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm

def browse(request):
    query = request.GET.get('query', '') 
    items = Item.objects.filter(Is_sold = False)
    categories = Categories.objects.all
    category_id = request.GET.get('category', 0)
    
    if query:
        items= items.filter(Q(Name__icontains=query) | Q(Description__icontains=query))
        
    if category_id:
        items = items.filter(category_id = category_id)

    return render(request, "item/browse.html", {"items" : items, "query" : query, "categories" : categories, "category_id" : int(category_id) })

def details(request, pk):
    item = get_object_or_404(Item , pk=pk)
    related_items = Item.objects.filter(Category = item.Category, Is_sold = False).exclude(pk = pk)[0:3]
    
    return render( request, "item/details.html",
                  {"item" : item, "related_items" : related_items} )

@login_required   
def add(request):
    form = NewItemForm
    
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit = False)
            item.User = request.user
            item.save()
            return redirect( 'dashboard:index')
    else : 
        form = NewItemForm
        
        
    return render(request, "item/form.html", {"form" : form})

@login_required
def delete(request, pk):
    item = get_object_or_404(Item , pk=pk, User = request.user)
    item.delete()
    
    return redirect('dashboard:index')
    


@login_required   
def edit(request, pk):
    form = EditItemForm
    item = get_object_or_404(Item, User = request.user, pk = pk)
    
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance = item)
        
        if form.is_valid():
            form.save()
            return redirect( 'dashboard:index')
    else : 
        form = EditItemForm(instance = item)
        
        
    return render(request, "item/form.html", {"form" : form})

