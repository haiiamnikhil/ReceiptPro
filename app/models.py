from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

GENDER_CHOICES = [
    ("MALE", "Male"),
    ("FEMALE", 'Female')
]

DOCTYPES_CHOICES = [
    ('RSD', 'RSD'),
    ('UPC', 'UPC'),
    ('RIN', 'RIN'),
    ('UPC-RSD', 'UPC-RSD'),
    ('RIN-RSD', 'RIN-RSD')
]


class CompanyWorker(models.Model):
    employ_id = models.CharField(max_length=20, blank=True)
    owner = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.owner


class Department(models.Model):
    company_department = models.CharField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.company_department


class Designation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.position

class EmployeeRole(models.Model):
    roles = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.roles
    
class Appointment(models.Model):
    status = models.CharField(max_length=50,unique=True, blank=True)

    def __str__(self):
        return self.status

class UserModel(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='user/profile_image', null=True, blank=True)
    phone = models.CharField(max_length=12, unique=True, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    emp_id = models.CharField(max_length=20, unique=True, blank=False, null=True)
    employ_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    employ_designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(null=True)
    shift_id = models.CharField(max_length=20, blank=True)
    team_lead_id = models.CharField(max_length=20, blank=True)
    team_lead_name = models.CharField(max_length=100, blank=True)
    team_lead_mail = models.EmailField(max_length=100, blank=True)
    company_worker_id = models.ForeignKey(CompanyWorker, on_delete=models.SET_NULL, null=True)
    employ_role = models.ForeignKey(EmployeeRole, on_delete=models.SET_NULL, null=True)
    appointment_status = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class UploadedDocument(models.Model):
    # name = models.CharField(max_length=100)
    files = models.FileField(upload_to='receipts/', default=0)
    doc_type = models.CharField(max_length=10, choices=DOCTYPES_CHOICES)
    # size = models.BigIntegerField(default=0)
    uploaded_by = models.ForeignKey(UserModel, to_field="username", on_delete=models.SET_NULL, null=True,
                                    related_name="user_documents")
    path = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    is_exported = models.BooleanField(default=False)

    def __str__(self):
        return self.doc_type


class UserStatus(models.Model):
    emp_name = models.ForeignKey(UserModel, to_field='username', on_delete=models.CASCADE, null=True)
    receipts_finished = models.CharField(max_length=256, blank=True, default=0)
    receipts_pending = models.CharField(max_length=256, blank=True, default=0)
    total_receipts_assigned = models.CharField(max_length=256, blank=True, default=0)

    def __str__(self):
        return self.emp_name


class ActiveUser(models.Model):
    name = models.ForeignKey(UserModel, to_field='username', on_delete=models.SET_NULL, null=True,
                             related_name="user_firstname")
    last_login = models.DateField(default=timezone.now)
    login_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name.first_name


class IndividualWorkAnalysis(models.Model):
    user_id = models.ForeignKey(UserModel, to_field="emp_id", on_delete=models.SET_NULL, null=True,
                                related_name="user_emp_id")
    username = models.ForeignKey(UserModel, to_field="username", on_delete=models.SET_NULL, null=True,
                                 related_name="user_username")
    assigned_by = models.ForeignKey(UserModel, to_field="username", on_delete=models.SET_NULL, null=True,
                                    related_name="user_assigned_by")
    assigned_on = models.DateTimeField(auto_now_add=True)
    file_id = models.ForeignKey(UploadedDocument, to_field='id', default=1, on_delete=models.SET_DEFAULT, null=True)
    completed_on = models.DateTimeField()

    def __str__(self):
        return self.username.first_name