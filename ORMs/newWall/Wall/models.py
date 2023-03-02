from __future__ import unicode_literals
from django.db import models
import bcrypt


class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}
        if len(postData['fname']) <= 0:
            errors["fname"] = "Must enter a first name!"
        elif len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters!"
        if len(postData['lname']) <= 0:
            errors["lname"] = "Must enter a last name!"
        elif len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters!"
        if len(postData['pword']) <= 0:
            errors["pword"] = "Password is required!"
        if len(postData['pword']) < 8:
            errors['pword'] = "Password must be at least 8 characters!"
        if len(postData['email']) <= 0:
            errors["email"] = "Email is required!"
        if User.objects.filter(email_address=postData['email']).exists():
            errors['email'] = "Email already exists."
        # if User.objects.filter(password = postData['pword']).exists():
        #     errors['pword'] = "Password already in use"
        if postData['confirm'] != postData['pword']:
            errors['confirm'] = "Confirmation password does not match password!"
        return errors

    def log_validation(self, postData):
        errors = {}
        try:
            user = User.objects.get(email_address=postData['email'])
        except:
            errors['email'] = f"Email address {postData['email']} is not registered in our database!"
            return errors
        if not bcrypt.checkpw(postData['pword'].encode(), user.password.encode()):
            errors['pword'] = "Password does not match our database!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # salt = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def hash_password(self, password):
        self.password = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password, hash_pw):
        return bcrypt.checkpw(password, hash_pw)


class Message(models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



