from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.base_user import AbstractBaseUser

from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.validators import UnicodeUsernameValidator





# classe de modification de gestion des utilisateur par defaut de django
class UserManager(BaseUserManager):

    def create_user(self,email,username,password=None,**extra_fields):
        if email is None:
            raise TypeError('le mail est obligatoire')
        user=self.model(email=self.normalize_email(email),username=self.normalize_email(username))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password=None,**extra_fields):
        user = self.create_user(
            
            email,
            username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    def email_user(self, *args, **kwargs):
        send_mail(
        '{}'.format(args[0]),
        '{}'.format(args[1]),
        '{}'.format(args[2]),
        [self.email],
        fail_silently=False,
    )



class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("Un utilisateur avec ce nom existe déjà."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
   
   
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    session_token = models.CharField(max_length=10, default=0)

    active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    # fontction personalisé pour envoie des messages à l'utilisateur
    def email_user(self, *args, **kwargs):
        send_mail(
        '{}'.format(args[0]),
        '{}'.format(args[1]),
        '{}'.format(args[2]),
        [self.email],
        fail_silently=False,
    )

    objects = UserManager()


# Create your models here.
