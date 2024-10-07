# library_manage/urls.py
from django.contrib import admin
from django.urls import path
from library import views  # Ensure this points to the correct app
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('library/', include('library.urls')),  # Include app URLs
    # You can include other apps similarly
    path('', RedirectView.as_view(url='/library/', permanent=False)),  # Redirect root URL

    
]
