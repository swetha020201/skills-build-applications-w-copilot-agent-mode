from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, LeaderboardEntry
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # Marvel team
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'bio': 'Genius, billionaire, playboy, philanthropist.', 'age': 48},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'bio': 'Super soldier.', 'age': 105},
            {'username': 'blackwidow', 'email': 'widow@marvel.com', 'bio': 'Master spy.', 'age': 35},
        ]
        for hero in marvel_heroes:
            user = User.objects.create_user(username=hero['username'], email=hero['email'], password='password')
            UserProfile.objects.create(user=user, bio=hero['bio'], age=hero['age'])
            marvel_team.members.add(user)
            Activity.objects.create(user=user, activity_type='Training', duration=60, date=date.today())
            LeaderboardEntry.objects.create(user=user, score=100)

        # DC team
        dc_team = Team.objects.create(name='Team DC')
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'bio': 'The Dark Knight.', 'age': 40},
            {'username': 'superman', 'email': 'superman@dc.com', 'bio': 'Man of Steel.', 'age': 35},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'bio': 'Amazonian warrior.', 'age': 3000},
        ]
        for hero in dc_heroes:
            user = User.objects.create_user(username=hero['username'], email=hero['email'], password='password')
            UserProfile.objects.create(user=user, bio=hero['bio'], age=hero['age'])
            dc_team.members.add(user)
            Activity.objects.create(user=user, activity_type='Training', duration=60, date=date.today())
            LeaderboardEntry.objects.create(user=user, score=100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with superhero test data.'))
