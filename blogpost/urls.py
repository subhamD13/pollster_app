from django.urls import path

from . import views

app_name = 'blogpost'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('details/<int:post_id>/', views.details, name='details'),
]
