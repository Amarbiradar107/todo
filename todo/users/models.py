from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100,default='')
    confirm_password = models.CharField(max_length=100,default='')

    def save(self, *args, **kwargs):
         # Hash password before saving
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name