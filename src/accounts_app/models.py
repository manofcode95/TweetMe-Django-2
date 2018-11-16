from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models.signals import post_save

User=get_user_model()
# Create your models here.

class UserProfileManager(models.Manager):
    def all(self):
        qs=self.get_queryset()
        if self.instance:
            qs=qs.exclude(user=self.instance)
        return qs

    def toggle_follow(self, request_user, to_toggle_user):
        current_userprofile, created=UserProfile.objects.get_or_create(user=request_user)
        if to_toggle_user in current_userprofile.get_following():
            current_userprofile.following.remove(to_toggle_user)
            added=False
        else:
            current_userprofile.following.add(to_toggle_user)
            added=True
        return added
    
    def is_following(self, request_user, to_toggle_user):
        if to_toggle_user in request_user.profile.get_following():            
            return True
        return False

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following= models.ManyToManyField(User,blank=True, related_name='followed_by')
    objects= UserProfileManager()

    def __str__(self):
        return self.user.username
    
    def get_following(self):
        return self.following.exclude(username=self.user)

    def get_follow_url(self):
        return reverse_lazy("profiles_app:toggle_follow", kwargs={'username':self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("profiles_app:user_detail", kwargs={'username':self.user.username})



def post_save_user_reciever(sender, instance, created, *args, **kwargs):
    if created:
        user_profile=UserProfile.objects.create(user=instance)
        return user_profile

post_save.connect(post_save_user_reciever, sender=User)