from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('create-topic/', views.page_create_topic, name='student_page_create_topic'),
]