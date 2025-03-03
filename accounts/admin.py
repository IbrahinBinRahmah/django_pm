from django.contrib import admin

from projects.models import Category, Project, Task
from . import models
# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Task)
