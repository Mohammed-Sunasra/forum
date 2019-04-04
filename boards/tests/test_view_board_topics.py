from django.urls import reverse, resolve
from django.test import TestCase
from ..models import Board
from ..views import home, board_topics, new_topic
from accounts.views import signup

class BoardTopicsTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django Board! ')
        url = reverse('board_topics', kwargs={'pk':self.board.pk})
        self.response = self.client.get(url)

    def test_board_topics_view_success_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_board_topics_view_notfound_code(self):
        url = reverse('board_topics', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_contains_link_back_to_home(self):
        home_page_url = reverse('home')
        self.assertContains(self.response, f'href="{home_page_url}"')
