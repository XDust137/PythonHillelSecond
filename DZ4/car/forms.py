from django import forms
from car.models import Car, CarModel, Company


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
