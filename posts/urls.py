from django.urls import path
from .views import add_post,edit_post,delete_post


urlpatterns=[
    path("add_post/",add_post,name="add_post"),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
]

