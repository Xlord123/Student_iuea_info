from django.contrib import admin
from .models import Staff,Department,Courses,Course_unit,Student

# Register your models here.
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Course_unit)
admin.site.register(Student)