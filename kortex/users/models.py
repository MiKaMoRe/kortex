from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from users.validations import (
    validate_first_name,
    validate_last_name,
)
from django.db import models


class UserWithEmailManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, verbose_name="email", unique=True)
    first_name = models.CharField(
        ("first name"), max_length=150, validators=[validate_first_name]
    )
    last_name = models.CharField(
        ("last name"), max_length=150, validators=[validate_last_name]
    )
    profile_picture = models.ImageField(
        blank=True,
        upload_to="profile_pictures",
        max_length=500,
    )
    profile_banner = models.ImageField(
        blank=True,
        upload_to="profile_banners",
        max_length=500,
    )
    slug = models.SlugField(
        ("custom id"),
        max_length=255,
        unique=True,
        null=False,
        db_index=True,
        editable=True,
    )

    objects = UserWithEmailManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.slug:
            last_user = User.objects.last()
            id = last_user.id if last_user else 0
            self.slug = f"id{id}"
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
