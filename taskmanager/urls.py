from django.contrib import admin
from django.urls import path, include  # The include function is used here
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # This includes the URLs from the tasks app
    path('', lambda request: redirect('tasks/', permanent=False)),  # Redirect root to 'tasks/'
]
