from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('walk_my_dog.walkmydog_auth.urls')),
                  path('', include('walk_my_dog.common.urls')),
                  path('', include('walk_my_dog.profiles_render.urls')),
                  path('', include('walk_my_dog.profile_auth.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
