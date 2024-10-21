from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    
    class Meta:
        verbose_name_plural = "items"
        ordering = ("Name",)
        
    
    def __str__(self):
        return self.Name
        
    Category = models.ForeignKey(Categories, related_name = "items", on_delete = models.CASCADE)
    Name = models.CharField(max_length = 255)
    Description = models.TextField(blank = True, null= True)
    Image = models.ImageField(upload_to = "item_images", blank = True, null= True)
    Price = models.FloatField()
    Is_sold = models.BooleanField(default = False)
    User = models.ForeignKey(User, related_name = "items", on_delete = models.CASCADE)
    Added_on = models.DateTimeField(auto_now_add = True)
    

