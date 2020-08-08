from django.contrib import admin
from .models import LessonCPD
from .models import SchoolCPD
# Register your models here.
admin.site.register(LessonCPD)
admin.site.register(SchoolCPD)