
class Barber:
    def __init__(self, level, services, name):
        self.level = level
        self.services = services
        self.name = name
        self.revenue = 0
        self.idle_time = 0
        self.work_days = 0
        self.max_service = 3
        self.current_service = 0
        self.completely_service = []

    def get_completely_service(self):
        return self.completely_service

    def add_completely_service(self, value):
        self.completely_service.append(value)
        return self.completely_service

    def set_revenue(self, value):
        self.revenue = value
        return self.revenue

    def get_current_service(self):
        return self.current_service

    def get_max_service(self):
        return self.max_service

    def set_current_service(self, value):
        self.current_service = value
        return self.current_service

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_services(self):
        return self.services

    def get_revenue(self):
        return self.revenue

    def get_idle_time(self):
        return self.idle_time

    def get_work_days(self):
        return self.work_days
