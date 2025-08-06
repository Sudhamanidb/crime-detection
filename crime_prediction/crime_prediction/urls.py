from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page URL, mapped to the home view
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    

     # Sign In page
    path('register/', views.register, name='register'),  # Register page
    path('emergency_alert/', views.emergency_alert, name='emergency_alert'),  # Emergency alert page

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files (CSS, JS, etc.)

