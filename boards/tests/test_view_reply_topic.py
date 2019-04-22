from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from ..models import Board, Topic, Post


class ReplyTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='This is a Django board!')
        self.username = "abcd"
        self.password = "123456"
        self.user = User.objects.create_user(username=self.username, email='john@doe.com',
                                            password=self.password)
        self.topic = Topic.objects.create(subject='Django is awesome!', board=self.board)
        Post.objects.create(message='Lorem Ipsum Test Post', topic=self.topic, created_by=self.user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})

    def LoginRequiredReplyPostTests(ReplyTopicTests):
        def test_login_required(self):
            pass