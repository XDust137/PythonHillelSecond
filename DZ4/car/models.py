from django.db import models
from django.urls import reverse


class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey(
        "car.CarModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )
    color = models.ForeignKey(
        "car.CarColor",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )

    def company(self):
        if self.car_model: return self.car_model.company
        return None
    def __str__(self): return f"Name:{self.name} vin_number: {self.vin_number}"
    def get_absolute_url(self): return reverse('car-detail', kwargs={'pk': self.pk})
    class Meta: ordering = ["car_model"]


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)
    def __str__(self): return self.name


class CarColor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name
    class Meta: verbose_name_plural = "Companies"


class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name
    class Meta: verbose_name_plural = "Companies"
