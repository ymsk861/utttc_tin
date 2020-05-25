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



##############################################
##############################################

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render
from cms.models import Todo, TodoForm

def index(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'cms/index.html', context)

def new(request):
    return render(request, 'cms/new.html')

def add(request):
    t1 = Todo()
    t1.todo_id = len(Todo.objects.order_by('-todo_id'))+1
    t1.update_date = timezone.now()
    t = TodoForm(request.POST, instance=t1)
    t.save()
    return HttpResponseRedirect(reverse('index'))

def detail(request, todo_id):
    todo = Todo.objects.get(todo_id=todo_id)
    context = {'todo': todo}
    return render(request, 'cms/new.html', context)

def update(request, todo_id):
    t1 = Todo.objects.get(todo_id=todo_id)
    t = TodoForm(request.POST, instance=t1)
    t.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, todo_id):
    t = Todo.objects.get(todo_id=todo_id)
    t.delete()
    return HttpResponseRedirect(reverse('index'))