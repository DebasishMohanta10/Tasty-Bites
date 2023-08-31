from django.contrib import admin
from .models import Category,MenuItem
# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'price')
    list_filter = ("category",)
    ordering = ("price",)
    search_fields = ("title","category__name")

admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(Category)
