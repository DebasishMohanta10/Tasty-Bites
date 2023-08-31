from django.db import models
from django_extensions.db.models import AutoSlugField

class Category(models.Model):
    title =  models.CharField(max_length=255,unique=True,db_index=True)
    slug =  AutoSlugField(max_length=255,unique=True,populate_from = ["title"])
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"

class MenuItem(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    slug = AutoSlugField(max_length=255,unique=True,populate_from = ["title"])
    price = models.DecimalField(max_digits=6,decimal_places=2,db_index=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
     
    
