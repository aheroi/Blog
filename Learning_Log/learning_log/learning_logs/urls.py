"""define URL schema for learning_logs"""

from django.urls import path
from .import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # # topic list page
    path('topics/', views.topics, name='topics'),
    ## page with details on a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # entries editing page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]