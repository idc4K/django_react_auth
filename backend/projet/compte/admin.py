from django.contrib import admin
from .models import User
class affichage(admin.ModelAdmin):
    list_display = ('first_name','email','date_joined','is_active','is_superuser','is_staff')
    search_fields = ['first_name']
admin.site.register(User,affichage)
# Register your models here.
