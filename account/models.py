from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, phone_No, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          phone_No= phone_No
      )

      user.set_password(password)
      user.is_user = True
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, phone_No, password=None):
      user = self.create_user(
          email,
          password=password,
          name=name,
          phone_No= phone_No
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  is_user = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  phone_No = models.CharField(max_length=150, null=True, blank=True)
  avatar = models.ImageField(upload_to="avatarimage/", null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name','phone_No']

  def __str__(self):
      return self.name

  def has_perm(self, perm, obj=None):
      return self.is_admin

  def has_module_perms(self, app_label):
      return True

  @property
  def is_staff(self):
      return self.is_admin
  

    
  





