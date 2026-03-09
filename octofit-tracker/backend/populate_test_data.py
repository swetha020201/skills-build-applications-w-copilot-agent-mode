from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, LeaderboardEntry
from datetime import date

# Create test user
test_user, created = User.objects.get_or_create(username='testuser', defaults={'email': 'testuser@example.com'})
test_user.set_password('testpass')
test_user.save()

# Create user profile
UserProfile.objects.get_or_create(user=test_user, defaults={'bio': 'Test bio', 'age': 30})

# Create activity
Activity.objects.get_or_create(user=test_user, activity_type='Running', duration=30, date=date.today())

# Create team and add user
team, created = Team.objects.get_or_create(name='Test Team')
team.members.add(test_user)
team.save()

# Create leaderboard entry
LeaderboardEntry.objects.get_or_create(user=test_user, defaults={'score': 100})

print('Test data populated successfully.')
