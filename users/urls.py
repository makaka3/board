from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login, sign_up, profile


app_name ="users"

urlpatterns = [
    path("login/", login, name = "login"),
    path("register/", sign_up, name = "register"),
    path("profile/", profile, name ="profile")
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

