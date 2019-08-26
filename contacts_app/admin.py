from django.contrib import admin
from contacts_app.models import Contact

# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display = ['manager', 'name', 'email', 'phone','info','date_added']
    list_filter = ['manager','date_added']

admin.site.register(Contact, AdminContact)