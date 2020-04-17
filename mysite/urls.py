
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('blogpost.urls')),
    path('todo/', include('todo.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
