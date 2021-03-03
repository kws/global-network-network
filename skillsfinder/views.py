from django.shortcuts import render
from django.views.generic import ListView, DetailView

from skillsfinder.models import Profile


class ProfileListView(ListView):
    paginate_by = 25
    model = Profile


class ProfileDetailView(DetailView):
    model = Profile
