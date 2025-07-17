from django.contrib import admin
from .models import Form, Course

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "email")
    readonly_fields = ("email",)

admin.site.register(Form, FormAdmin)

class CourseItemAdmin(admin.ModelAdmin):
    list_display = ("course_name", "price", "status")
    list_filter =  ("status",)
    search_fields = ("course_name", "description")

admin.site.register(Course, CourseItemAdmin)