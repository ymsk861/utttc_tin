from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
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

UserModel = get_user_model()


class TopView(TemplateView):
    template_name = 'cms/circleid-1-1.html'

class Next11View(TemplateView):
    template_name = 'cms/circleid-1-1.html'

class Next12View(TemplateView):
    template_name = 'cms/circleid-1-2.html'

class Next13View(TemplateView):
    template_name = 'cms/circleid-1-3.html'

class Next21View(TemplateView):
    template_name = 'cms/circleid-2-1.html'

class Next22View(TemplateView):
    template_name = 'cms/circleid-2-2.html'

class Next23View(TemplateView):
    template_name = 'cms/circleid-2-3.html'

class Next31View(TemplateView):
    template_name = 'cms/circleid-3-1.html'

class Next32View(TemplateView):
    template_name = 'cms/circleid-3-2.html'

class Next33View(TemplateView):
    template_name = 'cms/circleid-3-3.html'

class NextuseridView(TemplateView):
    template_name = 'cms/userid.html'

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


# -*- coding: utf-8 -*-

import json

from django.contrib import auth
from django.http import HttpResponse
from django.views import View


class BookmarkView(View):
    # This variable will set the bookmark model to be processed
    model = None
    def post(self, request, pk):
        # We need a user
        user = auth.get_user(request)
        # Trying to get a bookmark from the table, or create a new one
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # If no new bookmark has been created,
        # Then we believe that the request was to delete the bookmark
        if not created:
            bookmark.delete()
        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/json"
        )