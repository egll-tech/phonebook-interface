from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .models import Contact
from .services import ContactsService

# Create your views here.
class IndexView(ListView):
  paginate_by = 20
  template_name = 'index.html'
  context_object_name = 'contacts_list'
  service = ContactsService()
  filters = ("name", "phone_number", "address")
  
  def get_queryset(self):
      return self.service.get(self)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["title"] = "Contacts"
      context["search_name"] = self.request.GET.get(self.filters[0])
      context["search_phone_number"] = self.request.GET.get(self.filters[1])
      context["search_address"] = self.request.GET.get(self.filters[2])
      return context
  