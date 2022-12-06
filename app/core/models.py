"""
Database models
"""

from djago.db import models
from django.conntrib.auth.models import (
    AbstractBaseUser,
    BaseUerManager,
    PermissionsMixin
)

class UserManager(BaseUerManager):
    """Manager for users"""

    def create_user(self, email, password = None, **extra_field):
        """Create, save and return a neu user"""
        user = self.model(email = email, **extra_field)
        user.set_password(password)
        user.save(using = self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.Charfield(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
