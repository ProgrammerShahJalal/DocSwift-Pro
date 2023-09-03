from django.contrib import admin

# Register your models here.
from . models import User, ContactMessage

admin.site.register(User)
admin.site.register(ContactMessage)