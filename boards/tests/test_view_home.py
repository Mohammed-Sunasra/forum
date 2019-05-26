from django.urls import reverse, resolve
from django.test import TestCase
from ..models import Board
from ..views import BoardListView
from ..views import board_topics, new_topic
from accounts.views import signup


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='This is De-Jango Board! ')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/boards/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, f'href="{board_topics_url}"')