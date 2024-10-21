from django.shortcuts import render, redirect
from .forms import SignupForm


# Create your views here.
from items.models import Item, Categories

def index(request):
    items = Item.objects.filter(Is_sold = False)[0:6]
    categories = Categories.objects.all()
    return render(request, "core/index.html", {
        "categories" : categories, "items" : items
    })

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:   
        form = SignupForm()
        
    return render(request, "core/signup.html", {"form" : form})
