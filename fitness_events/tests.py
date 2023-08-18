from django.test import TestCase
from .models import Event, Registration

class FitnessEventsTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Fitness Expo',
            description='Join us for a fitness expo.',
            date='2023-08-15 10:00:00',
            location='Convention Center',
            is_published=True,
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.registration = Registration.objects.create(
            event=self.event,
            user=self.user,
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Fitness Expo')
        self.assertEqual(self.event.location, 'Convention Center')

    def test_registration_creation(self):
        self.assertEqual(self.registration.user.username, 'testuser')
