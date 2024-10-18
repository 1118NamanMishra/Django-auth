from django.contrib import admin
from django.urls import path, include  # Include 'include'
from users.views import landing_view  # Import the landing view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Make sure this line is present
    path('', landing_view, name='landing'),  # Set the landing page to redirect to register

]
