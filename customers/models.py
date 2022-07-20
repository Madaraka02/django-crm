from django.db import models
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
#  slug = AutoSlugField(populate_from='title')
class Client(models.Model):
    username = models.CharField(max_length=300, null=True, blank=True,unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    slug = AutoSlugField(populate_from='username')
    age = models.IntegerField(default=1, null=True, blank=True)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.username

