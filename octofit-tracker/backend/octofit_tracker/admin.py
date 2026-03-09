from django.contrib import admin
from .models import UserProfile, Activity, Team, LeaderboardEntry, Workout

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(LeaderboardEntry)
admin.site.register(Workout)
