from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    surname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    desc = models.TextField()  
    #date = models.models.models.DateField(_(""), auto_now=False, auto_now_add=False)

    def __str__(self):
            return self.email
    