# Basic tests for the API endpoints
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel', is_superhero=True)
        self.assertEqual(user.name, 'Test Hero')
        self.assertTrue(user.is_superhero)

    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Superhero team')
        self.assertEqual(team.name, 'Marvel')

    def test_activity_creation(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel', is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2026-03-02')
        self.assertEqual(activity.type, 'Running')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Superhero team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', suggested_for='Marvel')
        self.assertEqual(workout.name, 'Pushups')
