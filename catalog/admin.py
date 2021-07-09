from django.contrib import admin

# Register your models here.
from catalog.models import Student, Project, Department, Technology


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'school', 'email')

@admin.register(Project) 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_date', 'project_link')

admin.site.register(Department)
admin.site.register(Technology)