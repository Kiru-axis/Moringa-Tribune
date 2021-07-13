from django.contrib import admin
from .models import Article,Tags,MoringaMerch
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
# filter_horizontal allows ordering of many to many fields

# admin.site.register helps us add models to the admin page.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tags)
admin.site.register(MoringaMerch)
