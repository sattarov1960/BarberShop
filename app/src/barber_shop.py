

class Barbershop:
    def __init__(self):
        self._barbers = []
        self._clients = []
        self._queue = []
        self._services = []
        self._total_revenue = 0

    def getBarbers(self):
        return self._barbers

    def getServices(self):
        return self._services

    def getClients(self):
        return self._clients

    def getQueue(self):
        return self._queue

    def getTotalRevenue(self):
        return self._total_revenue

    def appendTotalRevenue(self, revenue):
        self._total_revenue += revenue

    def add_client(self, client):
        self.getClients().append(client)
        self.getQueue().append(client)

    def add_barber(self, barber):
        self.getBarbers().append(barber)

    def add_service(self, service):
        self._services.append(service)

    def simulate_client(self, client):
        for barber in self.getBarbers():
            if client.get_wait_time() >= client.get_max_time_wait():
                client.set_timeout(True)
                self.getQueue().remove(client)
                break
            if client.get_desired_service() in barber.get_services():
                if barber.get_current_service() > barber.get_max_service():
                    barber.set_current_service(barber.get_current_service() - 1)
                    continue
                else:
                    barber.set_current_service(barber.get_current_service() + 1)
                barber.add_completely_service(client.get_desired_service())
                barber.set_revenue(barber.get_revenue() + client.desired_service.get_price())
                self.appendTotalRevenue(client.desired_service.get_price())
                self.getQueue().remove(client)
                break
            else:
                client.set_wait_time(client.wait_time + 1)

    def simulate(self):
        for client in self.getQueue().copy():
            self.simulate_client(client)

    def average_wait_time(self):
        total_wait_time = sum([client.wait_time for client in self.getClients()])
        return total_wait_time / len(self.getClients())

    def unserved_clients(self):
        return len(self.getQueue())

    def get_timeout_clients(self):
        regular_clients = 0
        random_clients = 0
        for client in self.getClients():
            if client.get_timeout():
                if client.get_is_regular():
                    regular_clients += 1
                else:
                    random_clients += 1
        return random_clients, regular_clients

    def average_time_wait_client(self):
        total_time_wait = 0
        for client in self.getClients():
            total_time_wait += client.get_wait_time()
        return round(total_time_wait / len(self.getClients()), 2)

    def revenue_by_service_type(self):
        revenue_dict = {}
        for barber in self.getBarbers():
            for service in barber.get_completely_service():
                if service.get_category() not in revenue_dict:
                    revenue_dict[service.get_category()] = service.get_price()
                else:
                    revenue_dict[service.get_category()] += service.get_price()
        return revenue_dict

    def revenue_by_barber_level(self):
        revenue_barber_level = {}
        for barber in self.getBarbers():
            if barber.get_level() not in revenue_barber_level:
                revenue_barber_level[barber.get_level()] = barber.get_revenue()
            else:
                revenue_barber_level[barber.get_level()] += barber.get_revenue()
        return revenue_barber_level

    def revenue_by_barber(self):
        revenue_barber_text = ""
        for barber in self.getBarbers():
            revenue_barber_text += f"{barber.get_name()}={barber.get_revenue()} "
        return revenue_barber_text

    def revenue_barbershop(self):
        revenue_barbershop = 0
        for barber in self.getBarbers():
            revenue_barbershop += barber.get_revenue()
        return revenue_barbershop
