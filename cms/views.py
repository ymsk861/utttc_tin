from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class TopView(TemplateView):
    template_name = 'cms/top.html'