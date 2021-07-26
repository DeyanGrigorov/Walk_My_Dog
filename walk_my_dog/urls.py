
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('walk_my_dog.walkmydog_auth.urls')),
    path('', include('walk_my_dog.common.urls')),

]
