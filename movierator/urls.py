from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),  # rozszerza adres localhost/main/.... o wszystkie url zawarte w aplikacji main
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # pozwala wyświetlać zdjęcia z folderu moje_media w przeglądarce
