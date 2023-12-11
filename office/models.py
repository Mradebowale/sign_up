from django.db import models

# Create your models here.

class mail_user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.email