from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.browse, name = "browse"),
    path('<int:pk>/', views.details, name = "detail" ),
    path('new/', views.add, name = "add"),
    path('<int:pk>/delete/', views.delete, name = "delete"),
    path('<int:pk>/edit/', views.edit, name = "edit")    
]
