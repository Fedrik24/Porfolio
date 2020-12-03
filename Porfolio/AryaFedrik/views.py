from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class indexView(TemplateView):
    template_name = 'AryaFedrik/index.html'

class AboutView(TemplateView):
    template_name = 'AryaFedrik/about.html'

class WorkView(TemplateView):
    template_name = 'AryaFedrik/work.html'

class ContactView(TemplateView):
    template_name = 'AryaFedrik/contact.html'
