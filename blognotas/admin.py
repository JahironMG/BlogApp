from django.contrib import admin
from .models import  Post
# Register your models here.

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['autor','titulo','publicacion']
    ordering = ('publicacion',)

