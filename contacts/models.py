from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=250)
  phone_number = models.CharField(max_length=250)
  address = models.TextField()
  objects = models.Manager()
  def __str__(self):
    return self.name + " (" + self.phone_number + ")"

  class Meta:
    ordering = ["name"]