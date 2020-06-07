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

from .models import (Circle, Like, LikeForm)
import random

UserModel = get_user_model()
count = Circle.objects.all().count()
l = random.sample(range(1,count+1), k=count)
number = 0
x = 1

def index1(request):
    global x
    global l
    global number
    if request.user.is_authenticated:
        time = 1
        while True:
            i = l[number]
            if time > count:
                x = 0
                break
            elif not (Like.objects.filter(user=request.user, circle__circle_id=i).exists()):
                x = i
                break
            elif number < count - 1:
                number += 1
                time += 1
            else:
                number = 0
                time += 1
                l = random.sample(range(1, count + 1), k=count)
    data = Circle.objects.filter(circle_id=x)
    user = request.user
    params = {
        'data':data,
        'user':user
    }
    return render(request, 'cms/circleid-1-1.html', params)

def index2(request):
    data = Circle.objects.filter(circle_id=x)
    user = request.user
    params = {
        'data':data,
        'user':user
    }
    return render(request, 'cms/circleid-1-2.html', params)

def index3(request):
    data = Circle.objects.filter(circle_id=x)
    user = request.user
    params = {
        'data': data,
        'user': user
    }
    return render(request, 'cms/circleid-1-3.html', params)

def index21(request):
    data = Circle.objects.filter(circle_id=x)
    user = request.user
    params = {
        'data': data,
        'user': user
    }
    return render(request, 'cms/circleid-2-1.html', params)

def index22(request):
    data = Circle.objects.filter(circle_id=x)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-2-2.html', params)

def index23(request):
    data = Circle.objects.filter(circle_id=x)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-2-3.html', params)

def index31(request, circle_id):
    data = Circle.objects.filter(circle_id=circle_id)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-3-1.html', params)

def index32(request, circle_id):
    data = Circle.objects.filter(circle_id=circle_id)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-3-2.html', params)

def index33(request, circle_id):
    data = Circle.objects.filter(circle_id=circle_id)
    params = {
        'data':data
    }
    return render(request, 'cms/circleid-3-3.html', params)

def mylist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('../signup/')
    else:
        data = Like.objects.filter(user=request.user)
        params = {
            'data':data
        }
        return render(request, 'cms/userid.html', params)

def add(request):
    global x
    global number
    global l
    if not request.user.is_authenticated:
        return HttpResponseRedirect('../signup/')
    else:
        t1 = Like()
        t1.user = request.user
        circle = Circle.objects.get(circle_id=x)
        t1.circle = circle
        t = LikeForm(request.POST, instance=t1)
        t.save()
        time = 1
        while True:
            i = l[number]
            if time > count:
                x = 0
                break
            elif not (Like.objects.filter(user=request.user, circle__circle_id=i).exists()):
                x = i
                break
            elif number < count-1:
                number += 1
                time += 1
            else:
                number = 0
                time += 1
                l = random.sample(range(1, count + 1), k=count)
        return HttpResponseRedirect('../')

def dislike(request):
    global x
    global number
    global l
    if not request.user.is_authenticated:
        time = 1
        while True:
            i = l[number]
            x = i
            if number < count - 1:
                number += 1
            else:
                l = random.sample(range(1, count + 1), k=count)
                number = 0
            break
    else:
        time = 1
        while True:
            i = l[number]
            if time > count:
                x = 0
                break
            elif not (Like.objects.filter(user=request.user, circle__circle_id=i).exists()):
                x = i
                if number < count - 1:
                    number += 1
                else:
                    l = random.sample(range(1, count + 1), k=count)
                    number = 0
                break
            elif number < count - 1:
                number += 1
                time += 1
            else:
                number = 0
                time += 1
                l = random.sample(range(1, count + 1), k=count)
    return HttpResponseRedirect('../')

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


def delete(request, circle_id):
    Like.objects.filter(user=request.user, circle__circle_id=circle_id).delete()
    return HttpResponseRedirect('../../userid')

class AboutView(TemplateView):
    template_name = 'cms/about.html'

class KiyakuView(TemplateView):
    template_name = 'cms/kiyaku.html'

class PrivacyView(TemplateView):
    template_name = 'cms/privacy.html'