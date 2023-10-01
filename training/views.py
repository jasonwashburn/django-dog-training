from django.views.generic import DetailView, ListView, TemplateView

from .models import Pet


class HomePageView(TemplateView):
    template_name = "training/home.html"


class PetListView(ListView):
    model = Pet
    template_name = "training/pet_list.html"


class PetDetailView(DetailView):
    model = Pet
    template_name = "training/pet_detail.html"
