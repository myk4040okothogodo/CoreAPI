from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username :
            raise ValueError('Username is required')
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self,username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('first_name', "admin")
        extra_fields.setdefault('last_name', "admin")

        if not extra_fields.get("is_staff", False):
            raise ValueError('Superuser must have is_staff=True.')

        if not extra_fields.get("is_superuser", False):
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, email, password, **extra_fields)



class ImageUpload(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return str(self.image)


class UserProfile(models.Model):
    #user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    profile_picture = models.ForeignKey(ImageUpload, related_name="user_images", on_delete=models.SET_NULL, null=True)
    dob = models.DateField()
    phone = models.PositiveIntegerField()
    country_code = models.CharField(default="+234", max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class UserAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name="user_addresses", on_delete=models.CASCADE)
    street = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Nigeria")
    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_profile.user.email



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, default="yourfirstname")
    last_name = models.CharField(max_length=100, default="yourlastname")
    username = models.CharField(db_index=True, max_length=255, unique=True)
    user_address = models.OneToOneField(UserAddress, related_name="user_address",blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email','first_name','last_name']
    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().full_clean()
        super().save(*args, **kwargs)

