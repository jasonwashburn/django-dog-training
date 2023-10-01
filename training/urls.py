from django.urls import path

from .views import HomePageView, PetDetailView, PetListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("pets/", PetListView.as_view(), name="pet_list"),
    path("pets/<int:pk>/", PetDetailView.as_view(), name="pet_detail"),
]
