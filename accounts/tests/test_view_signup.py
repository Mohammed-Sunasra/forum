from django.test import TestCase
from django.urls import reverse, resolve
from ..views import signup, SignUpForm
from django.contrib.auth.models import User


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_page_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_view_function(self):
        view = resolve('/accounts/signup')
        self.assertEquals(view.func, signup)
    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_user_creation_model_form_type(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username':'testuser',
            'email':'test@test.com',
            'password1':'Test123456',
            'password2':'Test123456',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

    
class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, data={})

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
    
    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())