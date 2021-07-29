from django.urls import path

from walk_my_dog.info.views import how_it_works

urlpatterns = (
    path('how_it_works/', how_it_works, name='how it works'),
)
