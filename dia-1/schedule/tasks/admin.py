from django.contrib import admin
from tasks.models import Tasks


admin.site.site_header = "Tasks"
admin.site.register(Tasks)
