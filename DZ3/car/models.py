from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class CarColor(models.Model):
    color = [
        ('#FF0000', 'red'),
        ('#00FF00', 'green'),
        ('#FFFF00', 'yellow'),
        ('#0000FF', 'blue'),
        ('#FF00FF', 'pink'),
        ('#FFFFFF', 'white'),
        ('#000000', 'black'),
        ('#808080', 'gray'),
        ('#C0C0C0', 'silver')
    ]

    def __str__(self):
        return self.color


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"


class CarType(models.Model):
    car_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_type

    class Meta:
        verbose_name_plural = 'Car types'
        verbose_name = 'Car type'


class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey("car.CarModel", on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey("car.CarColor", on_delete=models.SET_NULL, null=True)
    product_date = models.DateField()
    car_type = models.ForeignKey("car.CarType", on_delete=models.SET_NULL, null=True)

    def company(self):
        return self.car_model.company

    def __str__(self):
        return f"Name:{self.name}; vin_number: {self.vin_number}; color: {self.color}"