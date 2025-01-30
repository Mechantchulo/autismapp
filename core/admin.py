from django.contrib import admin

# Register your models here.
from .models import UserProfile, BehaviorLog, Goal, Resource

admin.site.register(UserProfile)
admin.site.register(BehaviorLog)
admin.site.register(Goal)
admin.site.register(Resource)