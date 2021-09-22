from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from car.models import Car, CarModel, Company
from car.forms import CarForm, CarModelForm, CompanyForm
from django.views.generic.edit import CreateView


class CarListView(ListView):
    template_name = "car_list.html"

    model = Car
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of car",
            "list_len": len(context["car_list"])
        })
        return context


class CarDetailView(DetailView):
    """docstring for CarDetailView."""
    template_name = "car.html"
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarCreateView(CreateView):
    template_name = "car_create.html"

    model = Car
    form_class = CarForm


class CarModelListView(ListView):
    template_name = "car_list.html"

    model = CarModel
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of car",
            "list_len": len(context["car_list"])
        })
        return context


class CarModelDetailView(DetailView):
    template_name = "car.html"
    model = CarModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyCreateView(CreateView):
    template_name = "car_create.html"

    model = Company
    form_class = CompanyForm


class CompanyListView(ListView):
    template_name = "car_list.html"

    model = Company
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of companies",
            "list_len": len(context["car_list"])
        })
        return context


class CompanyDetailView(DetailView):
    template_name = "car.html"
    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
