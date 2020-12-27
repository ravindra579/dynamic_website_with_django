from django.contrib import admin
from .models import user,intern,projects,job
# Register your models here.
admin.site.register(user)
admin.site.register(intern)
admin.site.register(job)
admin.site.register(projects)