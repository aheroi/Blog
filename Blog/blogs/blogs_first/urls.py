"""define URLS schema for blogs_first"""

from django.urls import path

from .import views

app_name = 'blogs_first'
urlpatterns = [
    # home page
    path('', views.index, name='index'),            # page 410
    # page for new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]