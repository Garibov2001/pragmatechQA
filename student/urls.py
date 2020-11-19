from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('tags/', views.tags, name='student-tags'),
    path('tags/index', views.tag_info, name='student-tags-index'),
    path('about/', views.about, name='student-about'),
    path('rules/', views.rules, name='student-rules'),
    path('create-topic/', views.page_create_topic, name='student_page_create_topic'),
]