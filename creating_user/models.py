from django.db import models
from django.utils.timezone import now
from django.conf import settings
#User = settings.AUTH_USER_MODEL
#default=settings.AUTH_USER_MODEL.admin
from django.contrib.auth import get_user_model
User = get_user_model()
default = User.objects.get(username='bonas')

# Create your models here.
class Company_detail(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE,default=default)
    username = models.CharField(max_length=500,blank=True,null=True)
    name =  models.CharField(max_length=500,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    company_name = models.CharField(max_length=500,blank=True,null=True)
    properties_permission = models.BooleanField(default=False)
    tenants_permission = models.BooleanField(default=False)
    contracts_permission = models.BooleanField(default=False)
    owners_permission = models.BooleanField(default=False)
    time = models.TimeField(auto_now=True, blank=True)
    date = models.DateField(auto_now=True, blank=True)
    timestamp = models.DateTimeField(default=now)
    #verified = models.BooleanField(default=False)

    verified_status = (
        ('Yes','Yes'),
        ('No','No')
    )

    verified = models.CharField(
        max_length=100,
        choices=verified_status,
        blank=True,
        default='No'
    
        
    )





    ROLE_STATUS = (
        ('User', 'User'),
        ('Organization', 'Organization'),

        
    )

    role_status = models.CharField(
        max_length=100,
        choices=ROLE_STATUS,
        blank=True,
        default='User'
    
        
    )

    STATUS = (
        ('Active', 'Active'),
        ('Banned', 'Banned'),
        ('Close','Close')

        
    )

    status = models.CharField(
        max_length=100,
        choices=STATUS,
        blank=True,
        default='User'
    
        
    )

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return self.company_name


