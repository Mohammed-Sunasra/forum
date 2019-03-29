from django.urls import reverse, resolve
from django.test import TestCase
from .models import Board
from .views import home, board_topics, new_topic


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
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        print("Url is ", board_topics_url)
        self.assertContains(self.response, f'href="{board_topics_url}"')


class BoardTopicsTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django Board! ')
        url = reverse('board_topics', kwargs={'pk':self.board.pk})
        self.response = self.client.get(url)

    def test_board_topics_view_success_code(self):
        #url = reverse('board_topics', kwargs={'pk':1})
        #response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_board_topics_view_notfound_code(self):
        url = reverse('board_topics', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_contains_link_back_to_home(self):
        # board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        # response = self.client.get(url)
        home_page_url = reverse('home')
        self.assertContains(self.response, f'href="{home_page_url}"')


class NewTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django Board! ')
        url = reverse('new_topic', kwargs={'pk':self.board.pk})
        self.response = self.client.get(url)

    def test_new_topic_view_success_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_new_topic_view_not_found_code(self):
        url = reverse('new_topic', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/new')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_contains_link_back_to_home(self):
        home_page_url = reverse('home')
        self.assertContains(self.response, f'href="{home_page_url}"')

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, f'href="{board_topics_url}"')
