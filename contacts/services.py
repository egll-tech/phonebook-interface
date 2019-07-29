import requests
from .models import Contact


def get_remote_contacts():
    url = 'http://www.mocky.io/v2/581335f71000004204abaf83'
    req = requests.get(url, headers={'Connection': 'close'})
    if (req.status_code == 200):
        return req.json()['contacts']
    return []


def get_contacts(self):
    contacts = get_remote_contacts()
    for contact in contacts:
        Contact.objects.update_or_create(
            name=contact['name'], phone_number=contact['phone_number'], address=contact['address'])
    return Contact.objects.all()
