

from django.contrib import admin
from django.db.models import Count
from projects.models import Category, Project, Task
from . import models

admin.site.register(Category)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'category', 'created_at', 'tasks_count')
    list_per_page = 15
    list_editable = ['status']
    list_filter = ('category', 'user')

    def tasks_count(self, obj):
        return obj.tasks_count
    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'is_completed', 'project')
    list_editable = ['is_completed']
    list_per_page = 15

