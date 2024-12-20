from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'place')
    search_fields = ('place', 'phone')
    list_filter = ('place', 'phone')

admin.site.register(Student,StudentAdmin)
admin.site.register(Author)
admin.site.register(Book)

