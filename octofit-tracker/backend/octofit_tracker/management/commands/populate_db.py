from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

from django.conf import settings



# Sample data
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel"},
    {"name": "DC"},
]

ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Flight", "duration": 60},
    {"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 45},
    {"user_email": "ironman@marvel.com", "activity": "Suit Test", "duration": 30},
]

LEADERBOARD = [
    {"user_email": "superman@dc.com", "score": 100},
    {"user_email": "ironman@marvel.com", "score": 95},
]

WORKOUTS = [
    {"name": "Strength Training", "suggested_for": "DC"},
    {"name": "Tech Training", "suggested_for": "Marvel"},
]


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Insert Teams first (for FK integrity if needed)
        for team_data in TEAMS:
            Team.objects.create(**team_data)

        # Insert Users
        for user_data in USERS:
            User.objects.create(**user_data)

        # Insert Activities
        for activity_data in ACTIVITIES:
            Activity.objects.create(**activity_data)

        # Insert Leaderboard
        for lb_data in LEADERBOARD:
            Leaderboard.objects.create(**lb_data)

        # Insert Workouts
        for workout_data in WORKOUTS:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data using Django ORM.'))
