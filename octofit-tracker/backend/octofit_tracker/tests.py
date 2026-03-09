from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Activity, Team, LeaderboardEntry, Workout
    def test_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='A test workout', duration=45)
        self.assertEqual(workout.name, 'Test Workout')
from datetime import date

class OctofitTrackerTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        UserProfile.objects.create(user=user, bio='Test bio', age=30)
        Activity.objects.create(user=user, activity_type='Running', duration=30, date=date.today())
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        LeaderboardEntry.objects.create(user=user, score=100)

    def test_user_profile(self):
        profile = UserProfile.objects.get(user__username='testuser')
        self.assertEqual(profile.bio, 'Test bio')

    def test_activity(self):
        activity = Activity.objects.get(user__username='testuser')
        self.assertEqual(activity.activity_type, 'Running')

    def test_team(self):
        team = Team.objects.get(name='Test Team')
        self.assertEqual(team.members.count(), 1)

    def test_leaderboard(self):
        entry = LeaderboardEntry.objects.get(user__username='testuser')
        self.assertEqual(entry.score, 100)
