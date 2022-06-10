from django.db import models

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"
