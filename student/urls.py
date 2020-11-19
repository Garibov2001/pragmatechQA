from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('tags/', views.tags, name='student-tags'),
    path('tags/index', views.tag_info, name='student-tags-index'),
]