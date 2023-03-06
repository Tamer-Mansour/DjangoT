from django.db import models
import bcrypt


class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def hash_password(self, password):
        self.password = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password, hash_pw):
        return bcrypt.checkpw(password, hash_pw)
