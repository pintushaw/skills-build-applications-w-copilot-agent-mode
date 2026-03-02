from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='Marvel', is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team='Marvel', is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='DC', is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team='DC', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Flying', duration=120, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=200)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength training for superheroes', suggested_for='Marvel')
        Workout.objects.create(name='Flight Training', description='Flight skills for superheroes', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
