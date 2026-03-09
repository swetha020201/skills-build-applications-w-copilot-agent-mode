from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Activity, Team, LeaderboardEntry, Workout
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'age']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = LeaderboardEntry
        fields = ['user', 'score']
