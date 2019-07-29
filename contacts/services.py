import requests
from .models import Contact


class ContactsService:

    def get_remote_contacts(self):
        url = 'http://www.mocky.io/v2/581335f71000004204abaf83'
        req = requests.get(url, headers={'Connection': 'close'})
        if (req.status_code == 200):
            return req.json()['contacts']
        return []

    def update_db(self, contacts):
        for contact in contacts:
            Contact.objects.update_or_create(
                name=contact['name'], phone_number=contact['phone_number'], address=contact['address'])

    def search_contacts(self, request, filters):
        result = Contact.objects.get_queryset()
        for filter in filters:
            result = self.filter_by(result, request, filter)
        return result

    def filter_by(self, collection, request, parameter):
        var = request.GET.get(parameter)

        if var:
            return collection.filter(**{parameter + "__icontains": var})
        return collection

    def get(self, view):
        contacts = self.get_remote_contacts()
        self.update_db(contacts)
        return self.search_contacts(view.request, view.filters)
