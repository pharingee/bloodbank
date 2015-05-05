import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from django.db.models.loading import get_model


class Hospital(models.Model):

    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    number = models.CharField(max_length=15)


class UserManager(BaseUserManager):

    def create_user(
            self, email, first_name, last_name, hospital, contact_no,
            password):
        """
        Creates and saves a User with the given email,
        first_name, last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            contact_no=contact_no,
            hospital=hospital
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
            self, email, password, first_name, last_name, contact_no,
            hospital):
        """
        Creates and saves a superuser with the given email, password,
        first_name and last_name.
        """
        user = self.create_user(
            email, password=password, first_name=first_name,
            last_name=last_name, contact_no=contact_no)
        user.is_admin = True
        user.is_nbts = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(
        upload_to='media/avatars',
        blank=True,
        default=None,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=18)
    is_nbts = models.BooleanField(default=False)
    hospital = models.ForeignKey(
        Hospital, related_name='users', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact_no']

    def get_full_name(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def get_avatar(self):
        if self.avatar:
            return os.path.join(settings.S3_URL, self.avatar.name)
        else:
            return None

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def deactivate(self):
        self.is_active = False
        self.save()
        # user_deactivated.send(sender=self)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'users'


class UserActivity(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='activities')
    timestamp = models.DateTimeField(auto_now_add=True)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return '{} - {}'.format(self.title, str(self.user))
