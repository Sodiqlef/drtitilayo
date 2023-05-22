from django.contrib import admin
from .models import Journal, BookCount

# Register your models here.
admin.site.register(Journal)
admin.site.register(BookCount)
