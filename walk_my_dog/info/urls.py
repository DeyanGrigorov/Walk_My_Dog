from django.urls import path

from walk_my_dog.info.views import HowItWorksView

urlpatterns = (
    path('how_it_works/', HowItWorksView.as_view(), name='how it works'),
)
