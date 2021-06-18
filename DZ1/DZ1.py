import string
import random
import time

from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


class Car:
    name: str
    vin_number: str
    model: str

    def __str__(self):
        return 'name: ' + self.name + ', vin number: ' + self.vin_number + ', model: ' + self.model

    def __repr__(self):
        return 'name: ' + self.name + ', vin number: ' + self.vin_number + ', model: ' + self.model

    def __init__(self, name: str, vin_number: str = None, model: str = None):
        if vin_number is None: vin_number = ""
        if model is None:      model = ""
        self.name = name
        self.vin_number = vin_number
        self.model = model


class Human:
    name: str = None
    age: int = None
    current_car: Car = None
    cars: list = None

    def __init__(self, name: str, age: int = 18, cars=None):
        if cars is None: cars = []
        self.name = name
        self.age = age
        self.cars = cars

    def __str__(self):
        return 'name: ' + self.name + ', age: ' + str(self.age) + ', current car: \n' + str(self.current_car) + '\n' + \
               'cars: \n' + '\n'.join(map(str, self.cars))

    def __repr__(self):
        return 'name: ' + self.name + ', age: ' + str(self.age) + ', current car: \n' + str(self.current_car) + '\n' + \
               'cars: \n' + '\n'.join(map(str, self.cars))


def random_vin_generator():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))
    return res


# Запустить программу которая автоматически создасть 2 экземпляра человека и 10 экземпляров машин. У 10 машин могут
# быть одинаковые названия модели. Имя и вин номер машины должны генерироватся рандомно.
human1 = Human("George", 22)
human2 = Human("Michael", 19)
cars = [Car(fake.vehicle_make(), random_vin_generator(), fake.vehicle_year_make_model()) for i in range(10)]

for car in cars: random.choice([human1.cars, human2.cars]).append(car)

picked: str
isPicked = False

print('\n')
print(human1)
picked = input('\nWhich car do you want give to this human?\n>> ')

for car in human1.cars:
    if picked == car.name or picked == car.model or picked == car.vin_number:
        human1.current_car = car
        print('Great! Now ' + human1.name + ' drives on ' + human1.current_car.model + '!')
        isPicked = True
if not isPicked: print('Sorry, but he doesn\'t have this car yet, maybe some time later...')

isPicked = False
time.sleep(1)

print('\n')
print(human2)
picked = input('\nWhich car do you want give to this human?\n>> ')

for car in human2.cars:
    if picked == car.name or picked == car.model or picked == car.vin_number:
        human2.current_car = car
        print('Great! Now ' + human2.name + ' drives on ' + human2.current_car.model + '!')
        isPicked = True
if not isPicked: print('Sorry, but he doesn\'t have this car yet, maybe some time later...')

# YAAAAAAAY I FINALLY DID IT! I'm almost 100% sure that there will be a bunch of errors or possible simplification
# options, but finally seems like I understood the classes normally, how to work with them and what they are,
# and that's the first time I did the work with them FINALLY UNDERSTANDING WHAT I DO, because before I
# almost did not understand them
