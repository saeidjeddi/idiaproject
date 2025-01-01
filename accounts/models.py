from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="ایمیل",
        max_length=255,
        unique=True,
    )


    username = models.CharField(max_length=255, unique=True, verbose_name='نام کاربری')
    phone = models.CharField(max_length=11, unique=True, verbose_name='تلفن')
    is_active = models.BooleanField(default=True, verbose_name='فعال ')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone"]

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin