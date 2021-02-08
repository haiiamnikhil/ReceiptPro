from django.contrib import admin
from .models import *


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','date_joined', 'last_login', 'is_staff', 'is_active', 'is_superuser')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'position')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'files', 'is_completed', 'is_exported', 'uploaded_by', 'uploaded_at')


class IndividualWorkAnalysisAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_id', 'username', 'assigned_by')


class IndividualWorkAnalysisAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_id', 'username', 'assigned_by')


class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'last_login', 'login_status')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status')


class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ('pk','roles')

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(Department)
admin.site.register(Designation, DepartmentAdmin)
admin.site.register(CompanyWorker)
admin.site.register(UploadedDocument, DocumentAdmin)
admin.site.register(ActiveUser, ActiveUserAdmin)
admin.site.register(IndividualWorkAnalysis, IndividualWorkAnalysisAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(EmployeeRole,EmployeeRoleAdmin)