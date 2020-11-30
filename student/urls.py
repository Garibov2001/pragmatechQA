from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('about/', views.about, name='student-about'),
    path('rules/', views.rules, name='student-rules'),
    path('create-topic/', views.page_create_topic, name='student_page_create_topic'),
    path('user/<int:id>', views.user_activity, name='user_activity'),
    path('user/<int:id>/questions', views.user_questions, name='user_questions'),
    path('user/<int:id>/comments', views.user_comments, name='user_comments'),
    path('user/<int:id>/tags', views.user_tags, name='user_tags'),
    path('tags/', views.tags, name='tags'),
    path('tags/<slug:slug>', views.tag_info, name='single_tag'),
    path('faq', views.faq, name='faq'),
]