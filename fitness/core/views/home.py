from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse

from django.contrib.auth.models import User
from core.models import Activity
from core.forms.home import HomeForm


class HomeView(generic.TemplateView):
    template_name = 'home.html'
    form_class = HomeForm
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] =  User.objects.all()
        context['activities'] = Activity.objects.filter(active = True)

        data = {}
        for user in User.objects.all():
            data[user] = Activity.objects.filter(user = user, active = True)

        context["data"] = data
        return context

    def post(self, request):
        print(request.POST, request.GET)
        return redirect('home')
    
    # def form_valid(self, form):
    #     print(self.request.POST, self.request.GET)