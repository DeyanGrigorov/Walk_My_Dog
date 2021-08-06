from django.urls import path

from walk_my_dog.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='landing page'),
)
