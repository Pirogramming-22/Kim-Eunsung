from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    """Manager for custom user model."""
    def create_user(self, id, password=None, **extra_fields):
        """Create and return a regular user."""
        if not id:
            raise ValueError("The ID field must be set.")
        user = self.model(id=id, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(id, password, **extra_fields)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=50, primary_key=True, unique=True)  # 공통 ID
    password = models.CharField(max_length=128, blank=True, null=True)  # 비밀번호
    
    is_active = models.BooleanField(default=True)  # 활성화 여부
    is_staff = models.BooleanField(default=False)  # 직원 여부

    objects = UserManager()

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.id