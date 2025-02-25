from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete = models.CASCADE)
    age  = models.IntegerField()
    diagnosis = models.CharField(max_length = 100)
    preferences = models.TextField()

class BehaviorLog(models.Model):
    user_profile = models.ForeignKey(UserProfile , on_delete = models.CASCADE)
    behavior_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length = 100)

class Goal(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    goal_description = models.TextField()
    target_date = models.DateTimeField()
    achieved = models.BooleanField(default = False)

class Resource(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)