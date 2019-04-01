from django.urls import reverse, resolve
from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User

class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.response = self.client.post(reverse('password_reset'), {'email': 'john@doe.com'})
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[Django Boards] Please reset your password', self.email.subject)

    def test_email_to(self):
        self.assertEqual(['john@doe.com',], self.email.to)