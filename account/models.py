from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


class MyAccountManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'(?:\+7|8)(?:\d{2,3}){4}', message=
                                 'Телефон, должен быть в виде +79119119191 или 89559559595')
    phone = models.CharField(verbose_name='phone', validators=[phone_regex], max_length=12, unique=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    # TODO referral system
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_phone = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone'

    objects = MyAccountManager()

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True