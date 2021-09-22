import requests
import json


class Connector:
    server = "http://127.0.0.1:8000"
    api = "api"

    def __init__(self): self.session = requests.session()

    def url_maker(self, *items): return "/".join([self.server, *items]) + "/"

    def get_list(self, lc_model: str):
        res = self.session.get(self.url_maker(self.api, lc_model))
        if res.status_code != 200:
            print('exception!')
            print(res.status_code)
            print(res.text)
        return res.json()

    def create(self, lc_model: str, data):
        res = self.session.post(self.url_maker(self.api, lc_model), json=data)
        if res.status_code != 201:
            print('exception!')
            print(res.status_code)
            print(res.text)
        return res.json()

    def delete(self, lc_model: str, pk):
        res = self.session.delete(self.url_maker(self.api, lc_model, pk))
        if res.status_code != 204:
            print('exception!')
            print(res.status_code)
            print(res.text)
        return res


def run(connector):
    cmd = input('Universe Redactor > ')

    '''
    Галактики
    '''

    if cmd == 'create-galaxy' or 'cg':
        name = input('Name your galaxy: ')
        x = input('Size X: ')
        y = input('Size Y: ')
        shape = input('Shape: ')
        connector.create('Galaxy', {
            'name': name,
            'size_x': x,
            'size_y': y,
            'shape': shape,
        })
        print('Galaxy created successfully.')

    if cmd == 'list-galaxies' or 'lg':
        print('Your galaxies:')
        for galaxy in connector.get_list('Galaxy'):
            print(f'{galaxy["pk"]}. {galaxy["name"]} ({galaxy["size_x"]}, {galaxy["size_y"]}. {galaxy["shape"]})')

    if cmd == 'delete-galaxy' or 'cmd':
        pk = input('Type your galaxy ID to delete: ')
        print(connector.delete('Galaxy ', pk, ' deleted successfully.'))

    '''
    Звёздные системы
    '''

    if cmd == 'create-star-system' or 'css':
        name = input('Name your star system: ')
        x = input('Position X: ')
        y = input('Position Y: ')
        galaxy = input('Galaxy belongs to: ')

        connector.create('StarSystem', {
            'name': name,
            'position_x': x,
            'position_y': y,
            'galaxy': galaxy
        })
    if cmd == 'list-star-systems':
        for star_system in connector.get_list('StarSystem'):
            print(f'{star_system["pk"]}. {star_system["name"]} ({star_system["pos_x"]}, {star_system["pos_y"]}) galaxy: {star_system["galaxy"]}')

    if cmd == 'delete-star-system' or 'dss':
        pk = input('Type your star system ID to delete: ')
        print(connector.delete('StarSystem', pk, ' deleted successfully.'))

    '''
    Звёзды
    '''

    if cmd == 'create-star' or 'cs':
        name = input('Name your star: ')
        star_system = input('Star system belongs to: ')
        star_type = input('Type: ')
        diameter = input('Diameter: ')

        connector.create('Star', {
            'name': name,
            'star_type': star_type,
            'star_system': star_system,
            'diameter': diameter
        })
    if cmd == 'list-stars' or 'ls':
        for star in connector.get_list('Star'):
            print(f'{star["pk"]}. {star["name"]} d={star["diameter"]} {star["star_type"]} star system: {star["star_system"]}')

    if cmd == 'delete-star' or 'ds':
        pk = input('Star\'s ID to delete: ')
        print(connector.delete('Star ', pk, ' deleted successfully.'))

    '''
    Планеты
    '''

    if cmd == 'create-planet' or 'cp':
        name = input('Name your planet: ')
        color = input('Color: ')
        star_system = input('Star system belongs to: ')
        diameter = input('Diameter: ')
        age_in_centuries = input('Age in centuries: ')
        mass_in_suns = input('Mass in suns: ')
        atmosphere = input('What atmosphere?')
        habitable = input('Is habitable? (if empty - no, any value - yes)') != ''

        connector.create('Planet', {
            'name': name,
            'color': color,
            'star_system': star_system,
            'diameter': diameter,
            'age_in_centuries': age_in_centuries,
            'mass_in_suns': mass_in_suns,
            'atmosphere': atmosphere,
            'habitable': habitable
        })

    if cmd == 'list-planets' or 'lp':
        for planet in connector.get_list('Planet'):
            print(f'{planet["pk"]}. {planet["name"]} d={planet["diameter"]} {planet["color"]} is habitable: {planet["habitable"]} star system: {planet["star_system"]}')

    if cmd == 'delete-planet' or 'dp':
        pk = input('Planet\'s ID to delete: : ')
        print(connector.delete('Planet ', pk, ' deleted successfully.'))


def main():
    print('\"Choose action:\"')

    print('\"cg\" or \"create-galaxy\" - create galaxy')
    print('\"lg\" or \"list-galaxies\" - galaxies list')
    print('\"dg\" or \"delete-galaxy\" - delete galaxy')
    print()
    print('\"css\" or \"create-star-system\" - create star system')
    print('\"lss\" or \"list-star-systems\"  - create star systems list')
    print('\"dss\" or \"delete-star-system\" - delete create star system')
    print()
    print('\"cs\" or \"create-star\" - create star')
    print('\"ls\" or \"list-stars\"  - stars list')
    print('\"ds\" or \"delete-star\" - delete star')
    print()
    print('\"cp\" or \"create-planet\" - create planet')
    print('\"lp\" or \"list-planets\"  - planets list')
    print('\"dp\" or \"delete-planet\" - delete planet')

    connector = Connector()

    while True: run(connector)


if __name__ == '__main__': main()
