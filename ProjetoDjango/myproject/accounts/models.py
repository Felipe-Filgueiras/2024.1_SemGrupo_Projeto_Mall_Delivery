from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cnpj = models.CharField(max_length=14, unique=True, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    social_media_url = models.URLField(blank=True, null=True)
    store_address = models.CharField(max_length=255, null=True, blank=True)
    banner_image = models.ImageField(upload_to='banners/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bank_account = models.CharField(max_length=20, null=True, blank=True)
    bank_agency = models.CharField(max_length=20, null=True, blank=True)

    # Add related_name to groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A group represents a set of permissions.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
