from django.urls import path, include
from DZ3.car.views import car_view
urlpatterns = [
    path("car/", car_view ),
    path("car/<int:obj>", car_view ),
]
