from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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


class UserListView(ListView):
    model = Ads
    template_name = "newsfeed/user_ads.html"
    context_object_name = 'Ads'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ads.objects.filter(seller=user).order_by('-date_posted')


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
