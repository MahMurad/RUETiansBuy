from abc import ABC

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Ads


def home(request):
    context = {
        'Ads': Ads.objects.all()
    }
    return render(request, 'newsfeed/home.html', context)


class AdsListView(ListView):
    model = Ads
    template_name = "newsfeed/home.html"
    context_object_name = 'Ads'
    ordering = ['-date_posted']
    paginate_by = 5


class AdsDetailView(DetailView):
    model = Ads


class AdsCreateView(LoginRequiredMixin, CreateView):
    model = Ads
    fields = ['title', 'writer', 'category', 'subject', 'price', 'description', 'contact_no', 'photo']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reversed('ads-detail', kwargs={'pk': self.pk})


class AdsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ads
    fields = ['title', 'writer', 'category', 'subject', 'price', 'description', 'contact_no', 'photo']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.seller:
            return True
        return False


class AdsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ads
    success_url = '/'

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.seller:
            return True
        return False


def about(request):
    return render(request, 'newsfeed/about.html')
