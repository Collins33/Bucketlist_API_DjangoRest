from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class Bucketlist(models.Model):
    name = models.CharField(max_length = 255, blank=False, unique=True)
    owner = models.ForeignKey('auth.user',
    related_name='bucketlists',
    default= 0,
    on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """returns a human readable instance of a created model"""
        return "{}".format(self.name)


# create receiver to create the token
@receiver(post_save, sender = User)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

