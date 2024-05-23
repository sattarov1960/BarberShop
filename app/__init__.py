import random

from app.src.barber_shop import Barbershop
from app.src.service import Service
from app.utils.generate import create_barber, generate_client

barber_shop = Barbershop()
for service in [Service('Haircut', 'basic', 60, 500),
                Service('Shave', 'standard', 15, 250),
                Service('Coloring', 'complex', 60, 1000),
                Service('Painting nails', 'non-standard', 60, 2000)]:
    barber_shop.add_service(service)

for _ in range(random.randint(5, 10)):
    barber_lvl = ['beginner', 'experienced', 'master'][random.randint(0, 2)]
    barber_shop.add_barber(create_barber(services=barber_shop.getServices(), barber_lvl=barber_lvl))

for _ in range(random.randint(30, 50)):
    barber_shop.add_client(generate_client(
        services=barber_shop.getServices(),
        barbers=barber_shop.getBarbers()))
