from django.test import TestCase
from ..models import Board, Topic, Post
from ..views import topic_posts
from django.contrib.auth.models import User
from django.urls import reverse, resolve

class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django', description='This is a test django board!')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123456')
        topic = Topic.objects.create(subject='Hello world!', board=board, starter=user)
        Post.objects.create(message='Lorem Ipsum!', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)
    
    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_topic_posts_view_function(self):
        view = resolve('/boards/1/topics/1')
        self.assertEquals(view.func, topic_posts)
        
