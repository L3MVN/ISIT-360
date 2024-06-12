from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Department, Project, Employee

admin.site.site_header = "Administration"
admin.site.index_title = "Tune in, Rock out"
admin.site.site_title = "Amped Up"

class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ("name", "location")
    search_fields = ["name", "location"]
    ordering = ["name"]

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ("title", "start_date", "end_date")
    search_fields = ["title"]
    ordering = ["title"]

class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ("name", "birth_date", "department", "hire_date")
    search_fields = ["name", "department__name"]
    ordering = ["-hire_date"]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Employee, EmployeeAdmin)