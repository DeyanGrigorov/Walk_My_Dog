from django.urls import path

from walk_my_dog.common.views import landing_page

urlpatterns = (
    path('', landing_page, name='landing page'),
)
