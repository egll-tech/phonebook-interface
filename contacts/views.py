from django.shortcuts import render
from django.views import generic

from .models import Contact
from . import services

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'index.html'
  context_object_name = 'contacts_list'

  def get_queryset(self):
      return services.get_contacts(self)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["title"] = "Contacts"
      return context
  