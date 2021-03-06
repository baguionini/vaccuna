import os

from django.db import models

from core.models import AddressField, User


class LocalGovernmentUnit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='lgu')
    name = models.CharField(max_length=50)
    registrant_map = models.FileField(upload_to='maps/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


    def filename(self):
        return os.path.basename(self.registrant_map.name)


class VaccinationSite(models.Model):
    name = models.CharField(max_length=50)
    address = models.OneToOneField(AddressField, on_delete=models.CASCADE)
    lgu = models.ForeignKey(LocalGovernmentUnit, on_delete=models.CASCADE, related_name='vaccination_sites')
    daily_capacity = models.IntegerField()
    start_date = models.DateField(null=True)


class PriorityLocation(models.Model):
    name = models.CharField(max_length=50)
    address = models.OneToOneField(AddressField, on_delete=models.CASCADE)
    lgu = models.ForeignKey(LocalGovernmentUnit, on_delete=models.CASCADE, related_name='priority_locations')
    rank = models.IntegerField(null=True)
