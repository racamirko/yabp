from django.contrib import admin
from devblog.models import Story

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Story, StoryAdmin)
