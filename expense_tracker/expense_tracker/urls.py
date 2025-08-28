from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Include all tracker app URLs
    path('', include('tracker.urls')),  
]
