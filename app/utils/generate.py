import random
from typing import List

from app.src.barber import Barber
from app.src.service import Service
from app.src.client import Client

import names


def create_barber(services: List[Service], barber_lvl: str, barber_name: str = None):
    relation_sheet = {
        'beginner': ['basic'],
        'experienced': ['basic', 'standard'],
        'master': ['basic', 'standard', 'complex']
    }
    barber_services = relation_sheet.get(barber_lvl, [])
    barber_services.append('non-standard')
    name_barber = names.get_first_name(gender='male' if round(random.randint(0, 1)) else 'female')
    return Barber(level=barber_lvl,
                  services=[service for service in services if service.get_category() in barber_services],
                  name=name_barber)


def generate_client(services: List[Service],
                    barbers: List[Barber],
                    service: Service = None,
                    is_regular: bool = None,
                    max_time_wait: int = None,
                    custom_barber: Barber = None):
    service = service or services[random.randint(0, len(services) - 1)]
    is_regular = is_regular or bool(random.randint(0, 1))
    max_time_wait = max_time_wait or random.randint(0, 10)
    custom_barber = custom_barber or (None if round(random.randint(0, 1)) else barbers[random.randint(0, len(services) - 1)])
    return Client(desired_service=service,
                  is_regular=is_regular,
                  max_time_wait=max_time_wait,
                  preferred_barber=custom_barber)
