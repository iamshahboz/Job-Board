from django.test import TestCase
from account.models import User, University

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'surname': 'Doe',
            'name': 'John',
            'email': 'john@example.com',
            'role': User.RoleChoices.CANDIDATE
        }
        self.user = User.objects.create(**self.user_data)

    def test_user_creation(self):
        self.assertEqual(self.user.surname, 'Doe')
        self.assertEqual(self.user.name, 'John')
        self.assertEqual(self.user.email, 'john@example.com')
        self.assertEqual(self.user.role, User.RoleChoices.CANDIDATE)

    def test_user_deletion(self):
        user_id = self.user.id
        self.user.delete()
        self.assertIsNone(User.objects.filter(id=user_id).first())

class UniversityModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'name' : 'Almaty Management University'
        }
        self.university = University.objects.create(**self.user_data)
    
    def test_university_creation(self):
        self.assertEqual(self.university.name, 'Almaty Management University')

    def test_university_deletion(self):
        university_id = self.university.id
        self.university.delete()
        self.assertIsNone(University.objects.filter(id=university_id).first())
