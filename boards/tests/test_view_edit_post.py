from django.contrib.auth.models import User
from ..models import Board, Post, Topic
from django.urls import reverse, resolve
from ..views import PostUpdateView
from django.test import TestCase

class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board')
        self.username = 'John Doe'
        self.password = '1234'
        self.user = User.objects.create_user(self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Django Auth', board=self.board, starter=self.user)
        self.post = Post.objects.create(message='Lorem Ipsum', topic=self.topic, created_by=self.user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })

class LoginRequiredPostUpdateViewTests(PostUpdateViewTest):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, f'{login_url}?next={self.url}')


class UnauthorizedPostUpdateViewTests(PostUpdateViewTest):
    def setUp(self):
        super().setUp()
        username = 'jane'
        password = '123'
        user = User.objects.create_user(username=username, email='john@doe.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 404)