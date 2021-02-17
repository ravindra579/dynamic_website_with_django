from django.contrib import admin
from .models import user,interns,projects,job,icomment,jcomment
# Register your models here.
admin.site.register(user)
admin.site.register(interns)
admin.site.register(job)
admin.site.register(projects)
admin.site.register(icomment)
admin.site.register(jcomment)