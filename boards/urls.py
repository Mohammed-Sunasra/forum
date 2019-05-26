from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('<int:pk>', views.board_topics, name='board_topics'),
    path('<int:pk>/new', views.new_topic, name='new_topic'),
    path('<int:pk>/topics/<int:topic_pk>', views.topic_posts, name='topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/reply', views.reply_topic, name='reply_topic'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit', views.PostUpdateView.as_view(), name='edit_post'),
]
