from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView,
)

from .mixins import OnlyYouMixin
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)

from .models import (Circle,Like)

UserModel = get_user_model()

def index1(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-1-1.html', params)

def index2(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-1-2.html', params)

def index3(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-1-3.html', params)

def index21(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-2-1.html', params)

def index22(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-2-2.html', params)

def index23(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-2-3.html', params)

def index31(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-3-1.html', params)

def index32(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-3-2.html', params)

def index33(request):
    data = Circle.objects.filter(circle_id=1)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-3-3.html', params)

def mylist(request):
    data = Like.objects.filter(user=request.user)
    params = {
        'data':data
    }
    return render(request, 'cms/userid.html', params)

class Login(LoginView):
    form_class = LoginForm
    template_name = 'cms/login.html'

class Logout(LogoutView):
    pass

class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'cms/signup.html'
    success_url = reverse_lazy('cms:top')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class UserUpdate(OnlyYouMixin, UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'cms/user_update.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])

class UserDetail(DetailView):
    model = UserModel
    template_name = 'cms/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class UserList(ListView):
    model = UserModel
    template_name = 'cms/user_list.html'

class UserDelete(OnlyYouMixin, DeleteView):
    model = UserModel
    template_name = 'cms/user_delete.html'
    success_url = reverse_lazy('cms:top')


