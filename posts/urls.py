from django.conf.urls import url
from posts import views

# Here we define our urls and the corresponding views
urlpatterns = [
    url(r'^api/posts$', views.posts_list),
    url(r'^api/posts/(?P<pk>[0-9]+)', views.posts_details),
    url(r'^api/posts/published$', views.posts_list_published)
]

